# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import cv2


# %%
import os
os.sys.path


# %%
def main():
    imgpath="C:\\Users\\Kaustav\\Desktop\\MY CODE\\HOME Practice\\ANACONDA\\My First Image Processing Crash Course\\standard_test_images\\standard_test_images\\lena_color_256.tif"
    img = cv2.imread(imgpath,0)

    outpath = "C:\\Users\\Kaustav\\Desktop\\MY CODE\\HOME Practice\\ANACONDA\\My First Image Processing Crash Course\\output\\lena_color_256.tif"
    
    # Grayscale Image
    cv2.namedWindow('Lena', cv2.WINDOW_AUTOSIZE)
    cv2.imshow('Lena',img)
    cv2.imwrite(outpath,img)
    cv2
    cv2.waitKey(0)
    cv2.destroyWindow('Lena')

    # # Other modes
    # img = cv2.imread(imgpath,-1)
    # cv2.namedWindow('Lena', cv2.WINDOW_AUTOSIZE)
    # cv2.imshow('Lena',img)
    # cv2.waitKey(0)
    # cv2.destroyWindow('Lena')


if __name__ == "__main__":
    main()


# %%

