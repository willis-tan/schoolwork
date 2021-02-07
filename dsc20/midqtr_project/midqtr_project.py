"""
DSC 20 Mid-Quarter Project
Name: Willis Tan
PID:  A14522499
"""

# Part 1: RGB Image #
class RGBImage:
    """
    A blueprint for defining images as a 3-d matrix of color channels.
    All images have a red, green, and blue color channel.
    Each color channel is a matrix itself. Each element in a color channel's
    matrix represents the intensity of (red, green, or blue) at a pixel's
    position.
    """

    def __init__(self, pixels):
        """
        Constructor for the RGBImage class. 
        Instance attribute pixels initialized with the input pixels matrix 
        """
        # YOUR CODE GOES HERE #
        self.pixels = pixels  # initialze the pixels list here

    def size(self):
        """
        Returns the size of the resulting image. Size is determined as the
        number of rows and columns in the pixels matrix.

        Size is returned as tuple, (<# rows>, <# columns>)
        """
        # YOUR CODE GOES HERE #
        red_matrix = self.pixels[0]
        return (len(red_matrix), len(red_matrix[0])) # (row, column)

    def get_pixels(self):
        """
        Returns a copy of this instance's pixels list
        """

        return [[row[:] for row in channel] for channel in self.pixels]
        

    def copy(self):
        """
        Returns a copy this RGBImage instance. The copy has the same pixels
        list as the original.
        """
        # YOUR CODE GOES HERE #
        return RGBImage(self.get_pixels())

    def get_pixel(self, row, col):
        """
        Returns the color of a pixel at the given position as a triplet with
        the red, green, and blue intensity.

        (red intensity, green intensity, blue intensity) at row x col
        """
        # YOUR CODE GOES HERE #
        assert isinstance(row, int) and isinstance(col, int)
        dimension = self.size()
        assert 0 <= row < dimension[0]
        assert 0 <= col < dimension[1]

        BLUE_CHANNEL = 2

        red = self.pixels[0]
        green = self.pixels[1]
        blue = self.pixels[BLUE_CHANNEL]

        return (red[row][col], green[row][col], blue[row][col])

    def set_pixel(self, row, col, new_color):
        """
        Given color represented as a triplet of integers, set the color of the
        current pixel to be the new color. Ie, the 1st integer in new_color
        means replace the integer in the red component at the given position
        with the 1st integer. The same follows for green and blue.

        If any of the integers (intensity) in new_color is -1, do not update
        the intensity of the corresponding component.
        """
        # YOUR CODE GOES HERE #
        assert isinstance(row, int) and isinstance(col, int)
        dimension = self.size()
        assert -1 <= row < dimension[0]
        assert -1 <= col < dimension[1]

        component = 0
        for intensity in new_color:
            if intensity != -1:
                self.pixels[component][row][col] = intensity
            component += 1



# Part 2: Image Processing Methods #
class ImageProcessing:
    """
    Static methods that transform any given RGBImage instance by some manner,
    such as cropping and grayscaling.

    After a transformation, the transformed image is returned as a new
    RGBImage instance and the original is unaltered.
    """

    @staticmethod
    def negate(image):
        """
        Given an image, return a new image with its color negated.
        I.e, for each pixel with current intensity value val, the negative
        pixel will have intensity (255 - val).
        """
        # YOUR CODE GOES HERE #
        MAX_INTENSITY = 255
        matrix = image.get_pixels()

        func1 = lambda val: MAX_INTENSITY - val
        func2 = lambda y: list(map(func1, y))
        new_matrix = [list(map(func2, comp)) for comp in matrix]

        return RGBImage(new_matrix)


    @staticmethod
    def grayscale(image):
        """
        Given an image, set each intensity in all 3 color channels to be the
        average between the red, green, and blue intensity.

        I.e, let i be the row index, and let j be the column index
        r = red[i][j], red intensity at i,j
        g = green[i][j], green intensity at i,j
        b = blue[i][j], blue intensity at i,j

        average = (r + g + b) / 3

        red[i][j] = average, set red intensity at i,j to be the average
        green[i][j] = average, set green intensity at i,j to be the average
        blue[i][j] = average, set blue intensity at i,j to be the average
        """
        # YOUR CODE GOES HERE #
        size = image.size()
        rows, cols = size[0], size[1]

        def get_average(image, i, j):
            '''
            Given a position (i, j), get the 3 color intensities at the given 
            position and return the average value of the 3 values.
            '''
            BLUE_CHANNEL = 2
            DIVISOR_FOR_AVERAGE = 3

            pixel = image.get_pixel(i, j)
            r, g, b = pixel[0], pixel[1], pixel[BLUE_CHANNEL]
            avg = (r + g + b) // DIVISOR_FOR_AVERAGE
            return avg

        new_matrix = [[get_average(image, i, j) for j in range(cols)] \
            for i in range(rows)]

        return RGBImage([new_matrix, new_matrix, new_matrix])

    @staticmethod
    def scale_channel(image, channel, scale):
        """
        Given an image, an integer representing a color channel 
        (red, green, blue), and a scalar, scale all intensities in the given 
        image's corresponding color channel by the given scalar.

        If any intensity is scaled beyond 255, restrict the scaled intensity to
        255.
        """
        # YOUR CODE GOES HERE #
        MAX_INTENSITY = 255

        matrix = image.get_pixels()
        color = matrix[channel]
        scaler = lambda val: min(int(val * scale), MAX_INTENSITY)

        scaled = [[scaler(val) for val in row] for row in color]
        matrix[channel] = scaled

        return RGBImage(matrix)

    @staticmethod
    def clear_channel(image, channel):
        """
        Given an image and integer representing a color channel 
        (red, green, blue), set all intensities in the given image's 
        corresponding color channel to zero.
        """
        # YOUR CODE GOES HERE #
        matrix = image.get_pixels()
        color = matrix[channel]
        cleared = [[0 for elem in row] for row in color]
        matrix[channel] = cleared
        return RGBImage(matrix)

    @staticmethod
    def rotate_90(image, clockwise):
        """
        If clockwise = True, rotate the image 90 degrees clockwise.
        Else, rotate the image 90 degrees counterclockwise.
        """
        # YOUR CODE GOES HERE #
        matrix = image.get_pixels()

        if clockwise:
            return RGBImage([list(zip(*channel[::-1])) for channel in matrix])
        return RGBImage([list(zip(*channel))[::-1] for channel in matrix])

    @staticmethod
    def crop(image, tl_row, tl_col, target_size):
        """
        Starting from the starting position (tl_row, tl_col), crop the given
        image to the specified target_size (n_rows, n_cols). Return the cropped
        image.

        I.e, the cropped image is a n_row by n_col sized image whose top-left
        corner is the pixel at the starting position.

        If the target size is larger than possible, a smaller cropped image
        will be returned -> cropping stops when the last row and/or last column
        are reached.
        """
        # YOUR CODE GOES HERE #
        def crop_matrix(matrix):
            '''
            Given a color channel, crop the matrix to the specified size.
            Return a new color channel matrix that meets the target_size. The
            returned channel matrix's first element (0, 0), is the value in
            the original matrix at position (tl_row, tl_col).
            '''
            target_rows = target_size[0]
            target_cols = target_size[1]

            trunc_cols = [row[tl_col: tl_col + target_cols] for row in matrix]
            trunc_rows = trunc_cols[tl_row: tl_row + target_rows]
            return trunc_rows

        matrices = image.get_pixels()
        cropped = list(map(crop_matrix, matrices))
        return RGBImage(cropped)


    @staticmethod
    def chroma_key(chroma_image, background_image, color):
        """
        Given a chroma_image, a background_image, and a color, replace every
        pixel at position (i, j) in the chroma_image that is the same color as
        the given color with the pixel at (i, j) in the background_image.

        Return the altered image as a new RGBImage instance.
        """
        # YOUR CODE GOES HERE #
        assert all(
            isinstance(x, RGBImage) for x in [chroma_image, background_image]
        )
        assert chroma_image.size() == background_image.size()

        chroma_copy = chroma_image.copy()
        size = chroma_copy.size()
        rows, cols = size[0], size[1]

        for i in range(rows):
            for j in range(cols):
                pixel = chroma_copy.get_pixel(i, j)
                if pixel == color:
                    chroma_copy.set_pixel(i, j, background_image.get_pixel(i,j))

        return chroma_copy


# Part 3: Image KNN Classifier #
class ImageKNNClassifier:
    """
    Given a list of images and their respective descriptive labels as training
    data, this classifier will attempt to predict the label of any given image.

    The classifier uses the K-nearest-neighbors algorithm to determine the K
    most similar images to the input image based on their Euclidean distance.
    """

    def __init__(self, n_neighbors):
        """
        Constructor for ImageKNNClassifier class.

        Initialized with the amount of neighbors the classifier will use to
        make predictions. 
        """
        # YOUR CODE GOES HERE #
        self.n_neighbors = n_neighbors
        self.data = None

    def fit(self, data):
        """
        Input data is given as a list of tuples of the form 
        (<RGBImage_instance>, <string_label>)
        If this instance's does not already have data stored, store the given
        data.

        The length of the given data list must be greater than this instance's
        n_neighbors attribute.
        """
        # YOUR CODE GOES HERE #
        assert len(data) > self.n_neighbors
        assert self.data == None

        # data = [(img1, label1), (img2, label2), ..., (img_n, label_n)]
        self.data = data

    @staticmethod
    def distance(image1, image2):
        """
        Given two images, calculate and return the distance between them.

        First, both images have their pixels matrix flattened into 1-d vector 
        of their respective intensity values.
        Second, let the residual vector be the difference between image1's
        vector and image2's vector.
        Third, square every element in the residual vector.

        Distance is defined as the square root of the sum of all elements in
        the residual vector.
        """
        # YOUR CODE GOES HERE #
        assert image1.size() == image2.size()
        SQUARE = 2
        SQUARE_ROOT = 0.5

        matrix_1 = image1.get_pixels()
        matrix_2 = image2.get_pixels()

        flatten = lambda matrix: [val for channel in matrix \
                                      for row in channel \
                                      for val in row]

        vector_1, vector_2 = flatten(matrix_1), flatten(matrix_2)

        squares = [(vector_1[i] - vector_2[i])**SQUARE \
            for i in range(len(vector_1))]

        dist = (sum(squares))**SQUARE_ROOT
        return dist

    @staticmethod
    def vote(candidates):
        """
        Given a list of candidate labels, return the most common label.
        If there is a tie, return any of the tied labels.
        """
        # YOUR CODE GOES HERE #
        counts = dict()
        for label in candidates:
            if label not in counts:
                counts[label] = 1
            else:
                counts[label] += 1

        return max(counts, key=counts.get)

    def predict(self, image):
        """
        Given an input image, predict its label.

        Assuming this model has already been fitted with data, the model will
        determine the K most similar images to the input image.

        From those K images, return the label that appears the most often.
        """
        # YOUR CODE GOES HERE #
        assert self.data != None

        distances = [(self.distance(image, d[0]), d[1]) for d in self.data]
        distances.sort(key=lambda x: x[0])
        neighbors = distances[:self.n_neighbors]
        candidates = [item[1] for item in neighbors]

        return self.vote(candidates)
