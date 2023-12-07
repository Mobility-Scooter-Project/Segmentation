# Segmentation
Generates mask data from videos.

### Curent Notes/To-do List
* The pipeline current gets all frames into a list before processing them with models
* There may be an better way to process each frame at a time, but the intervals functionality makes it less efficient
* Needs to format data properly onto csv file
* Need to implement video writer feature