# Six Marimbas Visualizer
Documentation of progress with building a music visualizer for the Steve Reich composition "Six Marimbas" (1986)

"Six Marimbas" by Steve Reich is hopefully the piece of music that helps establish the visualization process I plan to use for converting the composer's more complicated works into a visual medium. This process is an attempt to translate the tonality of his compositions into combinations of colors, shapes, and animations that mimic the psychoacoustic moments resulting from Reich's repetitive and systematic composing style. By achieving this goal, I may translate my appreciation for his works with demonstrating the various ways in which Reich's music produces experiences that trascend merely the audial form.

Starting simple with Reich's smaller, single-instrument compositions is ideal for creating a system of audio-to-video transmutation before applying it to more complicated works. This first composition is ideal as a starting point for a data- and script-driven project due to a few convenient factors:

1. The only instrument in the piece is marimba. This means that if one were to translate an instrument into a shape, then only one shape is needed.
2. All notes played in the composition are eighth notes. The lack of diversity in note length may translate to more consistent animations.
3. While the piece is played at a fast tempo of 192 BPM, there is no variation in speed or note placement anywhere throughout its duration. This is typical of Reich's work which primarily focuses on music as a gradual process over a consistent pulse. Animating the piece is therefore easier than pieces that include ramps in speed due to note assignments coming down to mathematical precision, versus placing animations based on an artist's interpretation of the change in speed.

# Developing the Data

There are numerous recordings of "Six Marimbas" that can be used as the basis for the visualizer. However, the lack of a conductor or metronome and the direction given by Reich for the player to control the flow of the piece makes them inadequate for a video project where rigid timing is mandatory. This, of course, goes against Reich's own wishes for how the piece should be performed. Indeed, analyzing the original score published by Boosey & Hawkes results in every measure of the piece being notated with a suggested repetition count (e.g., "8x-12x", "2x-3x"), and entire sections where one marimba player is directed to advance to the next measure only when another player performing the same musical phrase advances to the next measure first. Despite this, visualizing the music at a rigid tempo may still provide insight into the visual translation of harmony inherent in the work. With a structure in place to optimize the placement of colors, shapes, and animations, further adjustments to adapt to actual recordings would become a practical exercise and could also produce interesting results in video form. The "data" of this project, therefore, is the music itself, interpreted in rigid structural form, in digital format.

## The Score

The score for "Six Marimbas" is written in the D-flat major scale, which consists of D-flat, E-flat, F, G-flat, A-flat, B-flat, and C notes, and is written in the 4/4 time signature. Players are given a suggested number of repeats for each measure, in a composition consisting of 163 total measures. The tempo is marked as 192 BPM with no ramps contained to modify the play speed internally. Players are, however, given directions for the strength of their playing, with the direction for the loudest playing given near the end ("ff", fortissimo, marimba 6, bar 153), and various moments of players being instructed to ramp down their playing volune to, and ramp up playing from, silence.

To translate the piece into data, Logic Pro was used to transcribe the written score into MIDI format (project files are not included in this repository). Three versions of the composition were produced in the software:

1. Base - The initial reconstruction of the composition. Features digital audio workspace productivity enhancements such as loops, automation, and panning to aid the process of transcription. Adjustments to the transcription were made here first and then adjusted into the versions explained below.
2. MIDI - The composition at its most basic form, panning is removed, automation on note velocity converted to flat integers, and loops rendered as solid regions, resulting in one audio block per instrument, which is then exported into separate MIDI files ("Six Marimbas Track 1", "Six Marimbas Track 2", etc.).
3. Audio - For use in the video, this version includes additional enhancements such as quantization randomization, variable note lengths and velocities, and mastering to mimic a realistic sound environment, which maintains a consistent structure. The resulting mix was then exported to lossless AIFF format ("Six Marimbas audio.aiff"), not included in this repository.

## The Conversion

The first part of translating MIDI files into usable data involves converting each file into CSV format using [MIDICSV](https://www.fourmilab.ch/webtools/midicsv/). This conversion maintains useful information from the MIDI files such as the timing of each note, what note is being played, and the velocity to which the note is being performed on the keyboard of a synthesizer. 

The CSV files produced by MIDICSV include various rows and columns of data that require filtering. Each CSV document starts with nine rows that describe the structural elements of the audio file, such as the name of the track, the name of the instrument playing the data, time signature of the file, key signature, and tempo. None of these rows are needed for video production and are discarded. Interspersed within the data are rows that indicate when a key on the keyboard is being pressed ("Note_on_c"), and when the key is being released ("Note_off_c"). Because the marimba does not feature the ability to sustain notes (aside from the velocity at which the mallet hits the metal bar prolonging note length), and because all notes in the composition are written as eighth notes, we do not need any rows that describe when the key of a synthesizer is released. That information is unnecessary. The Python script "MusicData.py" removes this unnecessary data after combining MIDI files into a Pandas DataFrame.

CSV documents also contain columns that provide no use, such as a column indicating when data is present (as opposed to identifying a row as data versus the beginning or end of a file), specific information in the header of the file, and additional columns used only for information contained within the header. All of this is removed by the script, as well.

"MusicData.py" then reformats the remaining information into usable information, which includes columns containing video timecodes for each note, structural data of the composition such as the section a note appears and which player is playing the note, and the pixel height the note appears in a video composition as well as which side of the marimba the note exists (either in the upper portion of the keyboard where groups of sharp and flats rest or in the lower portion of naturals).

## The Video

The final construction of the visualizer should take place in Blender, however initial experiments are being conducted in Adobe After Effects. Project files and exports are not included in this repository.

## Justification for method

ChatGPT was used for developing the following justification for using Paython and, more specifically, the Pandas package, to construct this project. This section will be rewritten eventually to be more cohesive, but I leave these points here to leave a record of their origination. Despite using an AI tool to generate these points, they remain points that I fully endorse.

Innovative Use of Technology: Leveraging Python for such a creative and interdisciplinary task is already a step outside the conventional use of the language, primarily known for web development, data science, and automation. This kind of innovative application showcases the versatility of Python as a programming language.

Appropriateness of Pandas: Given that your project involves complex data manipulation, which is exactly what Pandas excels at, its use is not only justified but also advantageous. The fact that the data isn't being used for traditional data science purposes doesn't diminish the utility Pandas brings to your project.

Setting a Precedent: Your project could serve as a precedent for others looking to perform similar interdisciplinary tasks. It demonstrates how tools commonly used in one domain (like Pandas in data science) can be effectively applied in another (like MIDI manipulation for video production).

Focus on End Goals: Ultimately, the choice of tools and libraries should be guided by the end goals of your project. If Pandas enables you to achieve those goals more efficiently and effectively, then its use is more than justified, regardless of the typical application domain.

Community and Documentation: Pandas is widely used and has a strong community and extensive documentation. This can be beneficial for both development and for users of your package, who may find it easier to understand and modify your code, if necessary.