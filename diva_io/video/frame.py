import numpy as np
from av import VideoFrame


class Frame(object):

    def __init__(self, frame: VideoFrame):
        self.frame = frame

    @property
    def frame_index_display(self) -> int:
        """The correct frame index for display, 0 based.

        Returns
        -------
        int
            Frame index for display.
        """
        return self.frame.pts - 1

    @property
    def frame_index_store(self) -> int:
        """The frame index as stored in the video, 0 based.
        If you used cv2.VideoCapture.read() to read a video sequentially, this 
        is the index you would get.

        Returns
        -------
        int
            Frame index as stored.
        """
        return self.frame.index

    def image(self):
        """Get PIL Image for visualization in jupyter.

        Returns
        -------
        PIL.Image
            Image for visualization in jupyter.
        """
        return self.frame.to_image()

    def numpy(self, format='bgr24', width: int = None,
              height: int = None) -> np.ndarray:
        """Get numpy array of the frame in the specified format.

        Parameters
        ----------
        format : str, optional
            Format parameter of av.VideoFrame.reformat(), by default 'rgb24'.
        width : int, optional
            Desired width of the frame, by default None
        height : int, optional
            Desired height of the frame, by default None

        Returns
        -------
        np.ndarray
            Numpy array of the frame.
        """
        return self.frame.to_ndarray(width=width, height=height, format=format)

    def __repr__(self):
        return '<%s contains %s>' % (
            repr(self.__class__)[8:-2], repr(self.frame))

    def __getattr__(self, name):
        return getattr(self.frame, name)
