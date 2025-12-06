### Transformations
transform tipocenter:
    xalign 0.5
    yalign 0.2

transform fade_text(fadein=0.8, hold=1.2, fadeout=1.0, color="#ffffff"):
    alpha 0.0
    linear fadein alpha 1.0
    pause hold
    linear fadeout alpha 0.0

transform fade_img(fadein=0.8, hold=1.2, fadeout=1.0, start_zoom=0.8, end_zoom=1.0):
    alpha 0.0
    zoom start_zoom
    xalign 0.5
    yalign 0.5
    linear fadein alpha 1.0 zoom end_zoom
    pause hold
    linear fadeout alpha 0.0