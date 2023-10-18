from dataclasses import dataclass

import numpy as np
import matplotlib.pyplot as plt

import streamlit as st


def init_image(size):
    return np.zeros((size, size, 3), np.uint8)


@dataclass
class GradientDef:
    red: tuple[int, int, bool]
    green: tuple[int, int, bool]
    blue: tuple[int, int, bool]


def get_gradient_2d(width, height, start, stop, is_horizontal):
    if is_horizontal:
        return np.tile(np.linspace(start, stop, width), (height, 1))
    else:
        return np.tile(np.linspace(start, stop, height), (width, 1)).T


def get_gradient_3d(width, height, g_def: GradientDef):
    result = np.zeros((height, width, 3), dtype=np.uint8)

    for i, color in enumerate([g_def.red, g_def.green, g_def.blue]):
        result[:, :, i] = get_gradient_2d(
            width,
            height,
            *color,
        )

    return result


# main !

# st.title("haha yeet")


s_col, e_col, d_col = st.columns(3)

with s_col:
    red0 = st.number_input(
        "red.start",
        min_value=0,
        max_value=255,
        value=0,
        key="red0",
    )

    green0 = st.number_input(
        "green.start",
        min_value=0,
        max_value=255,
        value=0,
        key="green0",
    )

    blue0 = st.number_input(
        "blue.start",
        min_value=0,
        max_value=255,
        value=0,
        key="blue0",
    )

with e_col:
    red1 = st.number_input(
        "red.end",
        min_value=0,
        max_value=255,
        value=255,
        key="red1",
    )

    green1 = st.number_input(
        "green.end",
        min_value=0,
        max_value=255,
        value=255,
        key="green1",
    )

    blue1 = st.number_input(
        "blue.end",
        min_value=0,
        max_value=255,
        value=255,
        key="blue1",
    )

with d_col:
    r_horizontal = st.toggle("red.horizontal", value=True, key="r_horizontal")
    g_horizontal = st.toggle("green.horizontal", value=True, key="g_horizontal")
    b_horizontal = st.toggle("blue.horizontal", value=True, key="b_horizontal")

w = 420
h = 270
g_def = GradientDef(
    red=(red0, red1, r_horizontal),
    green=(green0, green1, g_horizontal),
    blue=(blue0, blue1, b_horizontal),
)

g = get_gradient_3d(w, h, g_def)

fig, ax = plt.subplots(facecolor="none")
ax.imshow(g)
ax.axis("off")
st.pyplot(fig, use_container_width=True)
