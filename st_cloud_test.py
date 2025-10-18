import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl
from matplotlib import font_manager as fm
import os

# 日本語フォントの設定（システムにインストールされているフォントを探す）
font_dirs = ['/usr/share/fonts/']  # Linuxの一般的なフォントディレクトリ
font_files = fm.findSystemFonts(fontpaths=font_dirs)

# 見つかったフォントをMatplotlibに登録
for font_file in font_files:
    try:
        fm.fontManager.addfont(font_file)
    except:
        continue

# 日本語フォントファミリーを設定（複数のフォントを優先順位で指定）
plt.rcParams['font.family'] = ['IPAexGothic', 'Noto Sans CJK JP', 'MS Gothic', 'Yu Gothic']

def main():
    st.title("sin(x) のプロット")
    st.write("x ∈ [0, 2π] における sin(x) の折れ線グラフを表示します。")

    x = np.linspace(0, 2 * np.pi, 400)
    y = np.sin(x)

    fig, ax = plt.subplots(figsize=(8, 4))
    ax.plot(x, y, color="tab:blue", label="sin(x)")
    ax.set_title("Sin(x)のプロット")  # タイトルを追加
    ax.set_xlabel("x")
    ax.set_ylabel("sin(x)")
    ax.set_xlim(0, 2 * np.pi)
    ax.set_xticks([0, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi])
    ax.set_xticklabels(["0", "π/2", "π", "3π/2", "2π"])
    ax.grid(True, linestyle="--", alpha=0.5)
    ax.legend()

    st.pyplot(fig)

if __name__ == "__main__":
    main()
