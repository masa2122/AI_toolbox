
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft2, ifft2, fftshift
from PIL import Image, ImageDraw

import face_recognition
import cv2

def fft_change(image):
    # フーリエ変換
    f_transform = fft2(image)

    # フーリエ変換後の画像を周波数領域でシフト
    # f_transform_shifted = fftshift(f_transform)

    # ノイズの除去 (ここでは単純に高周波成分を0にする)
    cutoff_frequency = 148  # カットオフ周波数
    rows, cols = image.shape
    center_row, center_col = rows // 2, cols // 2
    f_transform[center_row - cutoff_frequency:center_row + cutoff_frequency,
                    center_col - cutoff_frequency:center_col + cutoff_frequency] = 0

    # フーリエ逆変換
    filtered_image = np.abs(ifft2(fftshift(f_transform)))
    filtered_image = np.uint8(filtered_image)
    
    return filtered_image

def detect(image_path):
    image2 = None
    origin = None
    
    # 顔のインポート
    load_img = face_recognition.load_image_file(image_path)
    face_locations = face_recognition.face_locations(load_img)
    if face_locations:
        # 切り出す場所を決める
        face_list = []
        value_max = 0
        # 認識された顔の文だけ繰り返す
        for (top, right, bottom, left) in face_locations:
            w = right - left
            h = bottom - top
            face_list.append([left,top])
            
            if w > h:
                value = w
            else:
                value = h

            if value_max < value:
                value_max = value
        
        # カラー画像の読み込み
        image = Image.open(image_path)
        image2 = image.copy()
        height,width,_ = np.array(image).shape
        
        # リサイズ
        size_x = int((100*width) / value_max)
        size_y = int((100*height) / value_max)
        # 元画像をグレイスケールでリサイズし配列にする
        image2 = np.array(image2.resize((size_x, size_y)).convert('L'))
        origin = image2.copy()
        # 画像を切り抜きフーリエ変換をしてから戻す
        for (x,y) in face_list:
            y_start = int((100*y)/value_max)
            x_start = int((100*x)/value_max)
            img = image2[y_start:y_start+100,x_start:x_start+100]
            img = fft_change(img)
            image2[y_start:y_start+100,x_start:x_start+100] = img
            

    else:
        print('顔を読み取れませんでした')
    return image2, origin

def main():
    st.title('自動モザイク')
    upload = st.file_uploader('画像を選択してください')
    if upload is not None:
        image_data, origin = detect(upload)
        if image_data is not None:
            fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))  # 1行2列のサブプロットを作成

            ax1.imshow(origin, cmap='gray')
            ax1.set_title('before')
            ax1.axis('off')  # 軸を非表示に設定

            ax2.imshow(image_data, cmap='gray')
            ax2.set_title('after')
            ax2.axis('off')  # 軸を非表示に設定
            
            st.pyplot(fig)

    
if __name__ == "__main__":
    main()