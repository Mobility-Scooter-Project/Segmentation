# Segmentation
Generates mask data from videos.

### Curent Notes
* MobileSAM version available in "fast" branch
* NanoSAM version available in "nano" branch

### System Environment
Jetson Orin Nano  
JetPack 5.1.3  
Python 3.8  
CUDA 11.4.19  
TensorRT 8.5.2  

### Performance
The following results were from processing 360 frames of video data. Also Includes data from running on laptop.
<table style="border-top: solid 1px; border-left: solid 1px; border-right: solid 1px; border-bottom: solid 1px">
    <thead>
        <tr>
            <th rowspan=2 style="text-align: center; border-right: solid 1px">Models</th>
            <th colspan=2 style="text-align: center; border-right: solid 1px">Jetson Orin Nano</th>
            <th colspan=2 style="text-align: center; border-right: solid 1px">NVIDIA GeForce RTX 2060</th>
        </tr>
        <tr>
            <th style="text-align: center; border-right: solid 1px">Total Time (s)</th>
            <th style="text-align: center; border-right: solid 1px">Average Frames per Second</th>
            <th style="text-align: center; border-right: solid 1px">Total Time (s)</th>
            <th style="text-align: center; border-right: solid 1px">Average Frames per Second</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td style="text-align: center; border-right: solid 1px">YOLOv8 + MobileSAM (No TensorRT)</td>
            <td style="text-align: center; border-right: solid 1px">233.82</td>
            <td style="text-align: center; border-right: solid 1px">1.54</td>
            <td style="text-align: center; border-right: solid 1px">TBD</td>
            <td style="text-align: center; border-right: solid 1px">TBD</td>
        </tr>
        <tr>
            <td style="text-align: center; border-right: solid 1px">YOLOv8 + NanoSAM (w/ TensorRT)</td>
            <td style="text-align: center; border-right: solid 1px">120.72</td>
            <td style="text-align: center; border-right: solid 1px">2.98</td>
            <td style="text-align: center; border-right: solid 1px">TBD</td>
            <td style="text-align: center; border-right: solid 1px">TBD</td>
        </tr>
    </tbody>
</table>