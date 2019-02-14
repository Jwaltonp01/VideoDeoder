import os
import time
import directory_info as di

import cv2


class VideoDecoder:
    def __init__(self):
        self.project_dir = di.get_project_dir()

    def make_temp_dir(self, dir_name):
        """
        Make tmp directory

        :param dir_name: desired tmp directory name
        :return:
            Temp directory
        """
        __tmp_dir = self.project_dir + "tmp/" + dir_name + "/"

        # Create directory
        try:
            # Create base directory
            if not os.path.exists(self.project_dir + "tmp/"):
                os.mkdir(self.project_dir + "tmp/")

            # Create directory for decoding video
            if not os.path.exists(__tmp_dir):
                os.mkdir(__tmp_dir)

        except OSError as e:
            print("Error creating file directory for video-data...")
            print(e.errno)

        return __tmp_dir

    def decode_video(self, vid_dir, output_dir, frame_save_rate=1):
        __tmp_dir = self.make_temp_dir(dir_name=output_dir)
        """Function to extract frames from input video file
        and save them as separate frames in an output directory.
        Args:
            input_loc: Input video file.
            output_loc: Output directory to save the frames.
        Returns:
            None
        """
        # Log the time
        time_start = time.time()
        # Start capturing the feed
        __cap = cv2.VideoCapture(vid_dir)
        # Find the number of frames
        video_length = int(__cap.get(cv2.CAP_PROP_FRAME_COUNT)) - 1
        print("Total frames: " + str(video_length))
        print("Number of save frames: " + str(int(video_length / frame_save_rate)))
        count = 0
        print("Converting video...\n")
        # Start converting the video
        while __cap.isOpened():
            # Extract the frame
            ret, frame = __cap.read()
            if count % frame_save_rate == 0:
                cv2.imwrite(__tmp_dir + "%#05d.jpg" % (count + 1), frame)
            count = count + 1
            # If there are no more frames left
            if count > (video_length - 1):
                # Log the time again
                time_end = time.time()
                # Release the feed
                __cap.release()
                # Print stats
                print("Done extracting frames.\n%d frames extracted" % (int(video_length / frame_save_rate)))
                print("Completed in %d seconds." % (time_end - time_start))
                break

        print("Video decoded to: " + __tmp_dir)
        return __tmp_dir


if __name__ == "__main__":
    vd = VideoDecoder()
    #
    vid_input = "FULL_PATH_TO_VIDEO"
    #
    output_name = "tmp_vid_output"
    #
    vd.decode_video(vid_dir=vid_input, output_dir=output_name, frame_save_rate=10)

