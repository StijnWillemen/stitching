def imagesplitter(imglist):
    length = len(imglist)
    imgs = []
    styled_imgs = []
    for i in range(length):
        if i >= length // 2:
            styled_imgs.append(imglist[i])
            continue
        imgs.append(imglist[i])
    return imgs,styled_imgs
