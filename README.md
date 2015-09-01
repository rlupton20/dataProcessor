# dataProcessor
A basic plugin architecture with GUI for doing data analysis.

New functionality can be added by writing a plugin to process the data, and adding it to the plugin folder. The plugin is then loaded on startup to give the new functionality.

A sample plugin estimates the initial growth of a curve, by minimizing r^2 over at least three points. An inspection tool is provided for inspecting the lines obtained and for checking problematic data sets.
