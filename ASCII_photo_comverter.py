import pygame as pyg
import numpy as np
import cv2


class ArtConvert:

    def __init__(self, path='image.jpg', font_s=12, color_level=32, chars='2', content=None):
        print("_init_")
        pyg.init()

        self.path = path
        self.content = content

        self.COLOR_LEVEL = color_level
        self.image, self.gray_image = self.get_image()
        self.RES = self.WiDTH, self.HEIGHT = self.image.shape[0], self.image.shape[1]
        self.surface = pyg.display.set_mode(self.RES)
        self.clock = pyg.time.Clock()
        if chars == '1':
            self.ASCII_CHARS = ' ●●●●●●●●●●●●●●●●●●●'
            # self.ASCII_CHARS = ' izxao*#MW&%B@'
        elif chars == '2':
            self.ASCII_CHARS = ' 01010101010101'
        elif chars == '3':
            self.ASCII_CHARS = ' ████████████████████████████'
        elif chars == '4':
            self.ASCII_CHARS = ' izxao*#MW&%B@'
        else:
            self.ASCII_CHARS = ' ' + chars

        self.ASCII_COEF = 255 // (len(self.ASCII_CHARS) - 1)
        self.ASCII_FONT = pyg.font.Font('unifont-15.0.06 (1).ttf', font_s)
        self.ASCII_FONT.set_bold(True)
        self.CHAR_STEP = int(font_s * 0.5)

        self.PALETTE, self.COLOR_COEF = self.palette()

    def draw_converted_image(self):
        print("draw_converted_image")
        char_indices = self.gray_image // self.ASCII_COEF
        color_indices = self.image // self.COLOR_COEF
        for x in range(0, self.WiDTH, self.CHAR_STEP):
            for y in range(0, self.HEIGHT, self.CHAR_STEP):
                char_index = char_indices[x, y]
                if char_index:
                    char = self.ASCII_CHARS[char_index]
                    color = tuple(color_indices[x, y])
                    self.surface.blit(self.PALETTE[char][color], (x, y))

    def palette(self):
        print("palette")
        colors, color_coeff = np.linspace(0, 255, num=self.COLOR_LEVEL, dtype=int, retstep=True)
        color_palette = [np.array([r, g, b]) for r in colors for g in colors for b in colors]
        palette = dict.fromkeys(self.ASCII_CHARS, None)
        color_coeff = int(color_coeff)
        for char in palette:
            char_palette = {}
            for color in color_palette:
                color_key = tuple(color // color_coeff)
                char_palette[color_key] = self.ASCII_FONT.render(char, False, tuple(color))
            palette[char] = char_palette
        return palette, color_coeff

    def get_image(self):
        print("get_image")
        cv2_content = np.frombuffer(self.content, np.uint8)
        self.cv2_image = cv2.imdecode(cv2_content, cv2.IMREAD_COLOR)
        print("image was loaded")

        """original_width, original_height = self.cv2_image.shape[1], self.cv2_image.shape[0]
        hd_width = 1920
        hd_height = hd_width * original_height/original_width
        self.cv2_image = cv2.resize(self.cv2_image, (hd_width, hd_height))"""

        transposed_image = cv2.transpose(self.cv2_image)
        gray_image = cv2.cvtColor(transposed_image, cv2.COLOR_RGB2GRAY)
        image = cv2.cvtColor(transposed_image, cv2.COLOR_BGR2RGB)
        return image, gray_image

    def draw_cv2_image(self):
        print("draw_cv2_image")
        resizwed_cv2_img = cv2.resize(self.cv2_image, (1280, 360), interpolation=cv2.INTER_AREA)
        cv2.imshow('img', resizwed_cv2_img)

    def draw(self):
        print("draw")
        self.surface.fill('black')
        self.draw_cv2_image()
        self.draw_converted_image()


    def save_image(self):
        print("save_image")
        pygame_image = pyg.surfarray.array3d(self.surface)
        cv2_img = cv2.transpose(pygame_image)
        cv2_img = cv2.cvtColor(cv2_img, cv2.COLOR_RGB2BGR)

        #cv2.imwrite('converted_image.jpg', cv2_img)

        self.image_bytes = cv2.imencode('.png', cv2_img)[1].tobytes()


    def save_image_WB(self):
        print("save_image")
        pygame_image = pyg.surfarray.array3d(self.surface)
        cv2_img = cv2.transpose(pygame_image)
        cv2_img = cv2.cvtColor(cv2_img, cv2.COLOR_RGB2GRAY)

        #cv2.imwrite('converted_image.jpg', cv2_img)

        self.image_bytes = cv2.imencode('.png', cv2_img)[1].tobytes()

    def run(self):
        print("run_image")
        self.draw()
        pyg.display.flip()
        self.save_image()
        return self.image_bytes

    def run_WB(self):
        print("run_image")
        self.draw()
        pyg.display.flip()
        self.save_image_WB()
        return self.image_bytes


def run(chars, font_s, file_content):
    app = ArtConvert(chars=chars, font_s=font_s, content=file_content)
    data = app.run()
    return data;
    exit()

def exp_run(chars, font_s,color ,file_content):
    app = ArtConvert(chars=chars, font_s=font_s, color_level=color,content=file_content)
    data = app.run()
    return data;
    exit()

def run_WB(chars, font_s, file_content):
    app = ArtConvert(chars=chars, font_s=font_s, content=file_content)
    data = app.run_WB()
    return data;
    exit()

if __name__ == '__main__':
    app = ArtConvert()
    app.run()