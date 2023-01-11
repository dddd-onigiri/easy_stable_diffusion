import streamlit as st
import numpy as np
from PIL import Image
from io import BytesIO

# 最初の画面
st.title("Brownian Motion")
st.header("Diffusion Simulation")

# 散乱したい元画像を選択
image_file = st.file_uploader("Upload your image", type="jpg")

if image_file is not None:
    image = Image.open(image_file)

# 作業用の画像を作成
image_arr = np.array(image)

size_x, size_y, size_z = image_arr.shape

# イージングのパラメーター
alpha = st.slider("alpha", 0.0, 1.0)
beta = st.slider("beta", 0.0, 1.0)

# 何回散乱を行うかを設定
N_iteration = st.slider("Iterations", 0, 50)

# 各値を用いて散乱を行う
for i in range(N_iteration):
    # 画像の中心座標を取得
    mid_x = int(size_x / 2)
    mid_y = int(size_y / 2)

    # 散乱させる位置を生成
    # ランダムな位置を生成
    x = int(np.random.uniform(0, size_x))
    y = int(np.random.uniform(0, size_y))

    # 画像を散乱させる
    image_arr[x, y] = np.array(
        [alpha * image_arr[x, y][0] + beta * image_arr[mid_x, mid_y][0],
         alpha * image_arr[x, y][1] + beta * image_arr[mid_x, mid_y][1],
         alpha * image_arr[x, y][2] + beta * image_arr[mid_x, mid_y][2]])

# 散乱させた画像を作成
image_out = Image.fromarray(image_arr.astype('uint8'))

# 画像を出力
st.image(image_out, use_column_width=True)

# test?
