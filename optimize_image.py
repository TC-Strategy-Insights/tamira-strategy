from PIL import Image
import os

input_path = "Tamira Carter.png"
output_path = "Tamira Carter_optimized.png"

try:
    print(f"Opening {input_path}...")
    with Image.open(input_path) as img:
        print(f"Original size: {img.size}")
        print(f"Original mode: {img.mode}")
        
        # Resize to 2x target size for retina displays (224 * 2 = 448px)
        # This keeps it crisp but much smaller than 1.8MB
        target_size = (450, 450)
        img.thumbnail(target_size, Image.Resampling.LANCZOS)
        
        print(f"New size: {img.size}")
        
        # Save with optimization
        img.save(output_path, "PNG", optimize=True)
        
    original_size = os.path.getsize(input_path)
    new_size = os.path.getsize(output_path)
    
    print(f"Optimization complete!")
    print(f"Original: {original_size/1024:.2f} KB")
    print(f"New: {new_size/1024:.2f} KB")
    print(f"Reduction: {(1 - new_size/original_size)*100:.1f}%")
    
except Exception as e:
    print(f"Error: {e}")
