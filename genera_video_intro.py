# -*- coding: utf-8 -*-
"""Genera un video introduttivo in stile 'codice battuto a macchina' + esecuzione Ruby."""
import os
import re
import imageio
import numpy as np
from PIL import Image, ImageDraw, ImageFont

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "intro_ruby.mp4")
FONT_CODE = "C:/Windows/Fonts/consola.ttf"
FONT_BOLD = "C:/Windows/Fonts/consolab.ttf"

W, H = 1280, 720
FPS = 30

CODE = """def sayhello(name)
  puts
  puts "This is the world of #{name}."
end

print "Enter your name here: "
sayhello(gets.chomp)
"""

INPUT_NAME = "Gabriel"


def font(size, bold=False):
    path = FONT_BOLD if bold else FONT_CODE
    return ImageFont.truetype(path, size)


def new_frame(bg=(30, 30, 30)):
    return Image.new("RGB", (W, H), bg)


def typing_frames(text, frames_per_char=2):
    frames = []
    acc = ""
    for _ in range(FPS // 2):
        frames.append(acc)
    for ch in text:
        acc += ch
        for _ in range(frames_per_char):
            frames.append(acc)
    for _ in range(FPS):
        frames.append(acc)
    return frames


def render_editor(typed):
    img = new_frame((30, 30, 34))
    d = ImageDraw.Draw(img)
    d.rectangle([(0, 0), (W, 40)], fill=(45, 45, 48))
    d.text((16, 8), "intro.rb  -  Ruby", font=font(18, bold=True), fill=(220, 220, 220))
    x0, y0 = 70, 70
    line_h = 34
    f = font(24)
    lines = typed.split("\n")
    for i, line in enumerate(lines):
        d.text((24, y0 + i * line_h), f"{i + 1:2d}", font=f, fill=(120, 120, 120))
    y = y0
    keywords = {"def", "end", "puts", "print"}
    for line in lines:
        x = x0
        for token in re.findall(r"\S+|\s+", line):
            color = (220, 220, 220)
            stripped = token.strip()
            if stripped in keywords:
                color = (86, 156, 214)
            elif stripped.startswith('"') or stripped.startswith("'") or "#{" in stripped:
                color = (206, 145, 120)
            d.text((x, y), token, font=f, fill=color)
            x += int(d.textlength(token, font=f))
        y += line_h
    if typed and not typed.endswith("\n"):
        last_line = lines[-1] if lines else ""
        cx = x0 + int(d.textlength(last_line, font=f))
        cy = y0 + (len(lines) - 1) * line_h
        d.rectangle([(cx, cy), (cx + 2, cy + 28)], fill=(220, 220, 220))
    d.rectangle([(0, H - 36), (W, H)], fill=(45, 45, 48))
    d.text((16, H - 28), "Premi Invio per eseguire...", font=font(16), fill=(180, 180, 180))
    return np.array(img)


def render_terminal(lines_output, cmd_typed=None, input_typed=None):
    img = new_frame((12, 12, 12))
    d = ImageDraw.Draw(img)
    f = font(24)
    lh = 34
    y = 40
    d.text((20, 8), "Terminal", font=font(18, bold=True), fill=(200, 200, 200))
    if cmd_typed is not None:
        d.text((20, y), "$ " + cmd_typed, font=f, fill=(100, 220, 100))
        y += lh
    if input_typed is not None:
        d.text((20, y), "Enter your name here: " + input_typed, font=f, fill=(220, 220, 220))
        y += lh
    for line in lines_output:
        d.text((20, y), line, font=f, fill=(220, 220, 220))
        y += lh
    return np.array(img)


def render_title():
    img = new_frame((20, 24, 40))
    d = ImageDraw.Draw(img)
    d.text((W // 2 - 260, H // 2 - 60), "GPuntobit", font=font(72, bold=True), fill=(86, 156, 214))
    d.text((W // 2 - 230, H // 2 + 20), "Introduzione a Ruby", font=font(36), fill=(220, 220, 220))
    d.text((W // 2 - 200, H // 2 + 70), "Codice battuto a macchina", font=font(24), fill=(160, 160, 160))
    return np.array(img)


def render_end():
    img = new_frame((20, 24, 40))
    d = ImageDraw.Draw(img)
    d.text((W // 2 - 180, H // 2 - 30), "Esecuzione completata!", font=font(40, bold=True), fill=(100, 220, 100))
    d.text((W // 2 - 210, H // 2 + 30), "Grazie per aver guardato", font=font(28), fill=(220, 220, 220))
    return np.array(img)


def main():
    writer = imageio.get_writer(OUT, fps=FPS, codec="libx264", quality=8)
    title = render_title()
    for _ in range(FPS * 2):
        writer.append_data(title)
    for partial in typing_frames(CODE, frames_per_char=2):
        writer.append_data(render_editor(partial))
    full_editor = render_editor(CODE)
    for _ in range(FPS):
        writer.append_data(full_editor)
    cmd = "ruby intro.rb"
    for partial in typing_frames(cmd, frames_per_char=3):
        writer.append_data(render_terminal([], cmd_typed=partial))
    inp_frames = typing_frames(INPUT_NAME, frames_per_char=3)
    for partial in inp_frames:
        writer.append_data(render_terminal([], cmd_typed=cmd, input_typed=partial))
    out_lines = ["", "This is the world of Gabriel."]
    for _ in range(FPS // 2):
        writer.append_data(render_terminal([], cmd_typed=cmd, input_typed=INPUT_NAME))
    shown = []
    for line in out_lines:
        shown.append(line)
        for _ in range(FPS // 2):
            writer.append_data(render_terminal(shown, cmd_typed=cmd, input_typed=INPUT_NAME))
    for _ in range(FPS * 2):
        writer.append_data(render_terminal(shown, cmd_typed=cmd, input_typed=INPUT_NAME))
    end = render_end()
    for _ in range(FPS * 2):
        writer.append_data(end)
    writer.close()
    print("Video creato:", OUT)


if __name__ == "__main__":
    main()
