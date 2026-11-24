import numpy as np
import cv2
import torch

class GradCAM:
    def _init_(self, model, target_layer):
        self.model = model
        self.target_layer = target_layer
        self.gradients = None
        self.activations = None
        
        # ग्रेडिएंट्स और एक्टिवेशन्स को कैप्चर करने के लिए हुक्स (Hooks) सेट करना
        self.target_layer.register_forward_hook(self.save_activation)
        self.target_layer.register_full_backward_hook(self.save_gradient)

    def save_activation(self, module, input, output):
        self.activations = output.detach()

    def save_gradient(self, module, grad_input, grad_output):
        self.gradients = grad_output[0].detach()

    def generate_heatmap(self, input_tensor, class_idx=None):
        # फॉर्वर्ड पास
        output = self.model(input_tensor)
        
        if class_idx is None:
            class_idx = torch.argmax(output, dim=1).item()
            
        # बैकवर्ड पास (चूने हुए क्लास के लिए ग्रेडिएंट निकालना)
        self.model.zero_grad()
        loss = output[0, class_idx]
        loss.backward()
        
        # ग्रेडिएंट्स का ग्लोबल एवरेज पूलिंग निकालना
        weights = torch.mean(self.gradients, dim=(2, 3), keepdim=True)
        
        # एक्टिवेशन मैप्स का वेटेड सम (Weighted Sum) करना
        cam = torch.sum(weights * self.activations, dim=1).squeeze(0)
        
        # ReLU अप्लाई करना (सिर्फ पॉजिटिव इन्फ्लुएंस वाले पिक्सेल रखने के लिए)
        cam = np.maximum(cam.cpu().numpy(), 0)
        
        # 0 से 255 के बीच नॉर्मलाइज़ करना
        if np.max(cam) != 0:
            cam = cam / np.max(cam)
        cam = cv2.resize(cam, (224, 224))
        heatmap = np.uint8(255 * cam)
        
        return heatmap

def overlay_heatmap(original_img_path, heatmap, alpha=0.5):
    """
    यह फंक्शन ओरिजिनल इमेज पर कलरफुल हीटमैप को ओवरले (मर्ज) करता है।
    """
    img = cv2.imread(original_img_path)
    img = cv2.resize(img, (224, 224))
    
    # हीटमैप को कलर मैप (JET) में बदलना
    color_heatmap = cv2.applyColorMap(heatmap, cv2.COLORMAP_JET)
    
    # दोनों इमेजेस को मर्ज करना
    overlayed = cv2.addWeighted(color_heatmap, alpha, img, 1 - alpha, 0)
    
    # OpenCV (BGR) से PIL (RGB) में बदलना ताकि Streamlit में दिखा सकें
    overlayed = cv2.cvtColor(overlayed, cv2.COLOR_BGR2RGB)
    return overlayed