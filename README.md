# Segmentation
Generates mask data from videos using YOLOv8, Segment Anything, MobileSAM, and NanoSAM.

### Curent Notes
* MobileSAM version available in "fast" branch
* NanoSAM version available in "nano" branch

### Setup
* Requires installation of YOLOv8 from ultralytics and its dependencies
* Requires installation of Segment Anything, MobileSAM, and NanoSAM and their dependencies

### Usage
```
python main.py -i INPUT_VIDEO -o OUTPUT_CSV -f FRAME_SKIP -v VIDEO_PATH
```
* `-i INPUT_VIDEO`
    * Path to input video
* `-o OUTPUT_CSV`
    * Path to CSV file to write coordinates
* `-f FRAME_SKIP`
    * OPTIONAL FLAG - Used to specify how many frames to skip each iteration
    * For example, `-f 6` would take every 6th frame of the video instead of all the frames
    * Defaults to 1 if unspecified, AKA takes every frame as the default
* `-v VIDEO_PATH`
    * OPTIONAL FLAG - Path to the processed video with the segmentation completed
    * If the flag is not specified, a video will not be generated

### System Environment
Jetson Orin Nano  
JetPack 5.1.3  
Python 3.8  
CUDA 11.4.19  
TensorRT 8.5.2  

### Performance
The following results were from processing 10800 frames of video data.
<table style="border-top: solid 1px; border-left: solid 1px; border-right: solid 1px; border-bottom: solid 1px">
    <thead>
        <tr>
            <th rowspan=2 style="text-align: center; border-right: solid 1px">Device</th>
            <th colspan=4 style="text-align: center; border-right: solid 1px">Average Time for 1 Frame (ms)</th>
            <!-- 
            <th colspan=2 style="text-align: center; border-right: solid 1px">NVIDIA GeForce RTX 2060</th>
            -->
        </tr>
        <tr>
            <th style="text-align: center; border-right: solid 1px">YOLOv8</th>
            <th style="text-align: center; border-right: solid 1px">YOLOv8 (TensorRT)</th>
            <th style="text-align: center; border-right: solid 1px">MobileSAM</th>
            <th style="text-align: center; border-right: solid 1px">NanoSAM</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td style="text-align: center; border-right: solid 1px">Jetson Orin Nano</td>
            <td style="text-align: center; border-right: solid 1px">40.24</td>
            <td style="text-align: center; border-right: solid 1px">37.28</td>
            <td style="text-align: center; border-right: solid 1px">345.78</td>
            <td style="text-align: center; border-right: solid 1px">61.28</td>
        </tr>
        <!--
        <tr>
            <td style="text-align: center; border-right: solid 1px">YOLOv8 + NanoSAM (w/ TensorRT)</td>
            <td style="text-align: center; border-right: solid 1px">120.72</td>
            <td style="text-align: center; border-right: solid 1px">2.98</td>
            <td style="text-align: center; border-right: solid 1px">65.20</td>
            <td style="text-align: center; border-right: solid 1px">5.52</td>
        </tr>
        -->
    </tbody>
</table>