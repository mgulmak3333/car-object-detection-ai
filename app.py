from ultralytics import YOLO
import streamlit as st 
from PIL import Image


st.title('Voren-X1 | Cars Detection AI')
model = YOLO('voren.pt')

file_upload = st.file_uploader('File Upload', type=['png', 'jpg'], accept_multiple_files=True)

if file_upload is not None:
    
    for file in file_upload:
        
        image = Image.open(file).convert('RGB')
        col1, col2 = st.columns(2)
        
        with col1:
            st.image(image, caption='Before', use_container_width=True)
            
        with col2:
            results = model.predict(source=image, imgsz=512, device='cpu')
            
            response_img = results[0].plot()
            st.image(response_img, caption='After', use_container_width=True, channels='BGR')
            
        count_car = len(results[0].boxes)
        st.success(f'Number of Vehicles: {count_car}')
        
        st.divider()