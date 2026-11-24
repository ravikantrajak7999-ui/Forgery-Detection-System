import os
from PIL import Image, ImageChops, ImageEnhance
import numpy as np

# Error Level Analysis (ELA) फ़ंक्शन - जो फोर्जरी के निशानों को उजागर करता है
def compute_ela(image_path, quality=90):
    temp_filename = 'temp_ela.jpg'
    
    # 1. ओरिजिनल इमेज लोड करें
    image = Image.open(image_path).convert('RGB')
    
    # 2. इसे कम क्वालिटी पर सेव करें
    image.save(temp_filename, 'JPEG', quality=quality)
    temporary = Image.open(temp_filename)
    
    # 3. पिक्सेल का अंतर (Absolute Difference) निकालें
    ela_image = ImageChops.difference(image, temporary)
    
    # 4. कंट्रैस्ट बढ़ाएं ताकि एडिटेड हिस्से साफ़ दिखें
    # टुपल और लिस्ट के झंझट से बचने के लिए इसे सीधे नम्पाई (numpy) एरे में बदलें
    ela_arr = np.array(ela_image)
    max_diff = np.max(ela_arr)
    
    if max_diff == 0:
        max_diff = 1
        
    scale = 255.0 / max_diff
    
    # ब्राइटनेस बढ़ाकर री-स्केल करें
    ela_image = ImageEnhance.Brightness(ela_image).enhance(scale)
    
    # टेम्परेरी फाइल को डिलीट करें
    if os.path.exists(temp_filename):
        os.remove(temp_filename)
        
    return ela_image.convert('RGB')

# जांचने के लिए मेन फ़ंक्शन
if __name__ == "__main__":
    print("Preprocessing script successfully")
