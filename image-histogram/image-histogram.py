def image_histogram(image):
    """
    Compute the intensity histogram of a grayscale image.
    """
    mapping = [0] * 256
    for row in image:
        for x in row:
            mapping[x] +=1
    return mapping