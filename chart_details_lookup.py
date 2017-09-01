#!/usr/bin/env python
# encoding: utf-8

'''
global_specs sets up some global variables for the plots
'''

global_specs = {
    'plot_width': 8,
    'plot_height': 5.8,
    'font_name': 'Serif'
    }

'''
plot_details is a dictionary of lists. The lists are of the form:
 0. Plot type
 1. the file in which the data  is stored
 2. first column to plot
 3. second column to plot (or False, if none)
 4. title for x axis, or use False if no title to be shown
 5. rotation of x-axis tick labels (0 is horizontal)
 6. max length of x-axis tick labels before they start a new line
 7. title for y axis, or use False if no title to be shown
 8. title of chart, or use False if no title
 9. whether to show value labels on bars (True/False)
10. how many labels to remove after each one shown (or False to keep all)
11. fraction of chart dedicated to x-axis tick labels (0-1)
12. size of title font
13. size of axis fonts
14. size of value label font
'''


plot_details = {
    'edu1': {
            'filename': 'edu1.csv',
            'plot_type': 'bar',
            'y1_axis': 'percentage',
            'y2_axis': False,
            'x_title': False,
            'x_rot': 0,
            'x_max_len': 15,
            'y_title': 'Percentage',
            'chart_title': 'Education level',
            'show_values': True,
            'skip_labels': False,
            'bottom_size': 0.1,
            'title_font_size': 24,
            'axis_font_size': 14,
            'value_font_size': 24
            },
    'edu2': {
            'filename': 'edu2.csv',
            'plot_type': 'bar',
            'y1_axis': 'percentage',
            'y2_axis': False,
            'x_title': False,
            'x_rot': 45,
            'x_max_len': 15,
            'y_title': 'Percentage',
            'chart_title': 'Education background',
            'show_values': True,
            'skip_labels': False,
            'bottom_size': 0.3,
            'title_font_size': 24,
            'axis_font_size': 10,
            'value_font_size': 14
            },
    'edu2p2': {
            'filename': 'edu2p2.csv',
            'plot_type': 'bar',
            'y1_axis': 'percentage',
            'y2_axis': False,
            'x_title': False,
            'x_rot': 45,
            'x_max_len': 15,
            'y_title': 'Percentage',
            'chart_title': 'Top 10 backgrounds',
            'show_values': True,
            'skip_labels': False,
            'bottom_size': 0.25,
            'title_font_size': 24,
            'axis_font_size': 14,
            'value_font_size': 20
            },
    'currentEmp1': {
             'filename': 'currentEmp1.csv',
             'plot_type': 'bar',
             'y1_axis': 'percentage',
             'y2_axis': False,
             'x_title': False,
             'x_rot': 45,
             'x_max_len': 15,
             'y_title': 'Percentage',
             'chart_title': 'Where do you work?',
             'show_values': True,
             'skip_labels': False,
             'bottom_size': 0.28,
             'title_font_size': 24,
             'axis_font_size': 12,
             'value_font_size': 20
             },
    'currentEmp13': {
             'filename': 'currentEmp13.csv',
             'plot_type': 'bar',
             'y1_axis': 'percentage',
             'y2_axis': False,
             'x_title': False,
             'x_rot': 45,
             'x_max_len': 15,
             'y_title': 'Percentage',
             'chart_title': 'In which field do you work?',
             'show_values': False,
             'skip_labels': 2,
             'bottom_size': 0.28,
             'title_font_size': 24,
             'axis_font_size': 12,
             'value_font_size': 20
             },
    'currentEmp13p2': {
             'filename': 'currentEmp13p2.csv',
             'plot_type': 'bar',
             'y1_axis': 'percentage',
             'y2_axis': False,
             'x_title': False,
             'x_rot': 45,
             'x_max_len': 15,
             'y_title': 'Percentage',
             'chart_title': 'Top 10 fields of work',
             'show_values': True,
             'skip_labels': False,
             'bottom_size': 0.28,
             'title_font_size': 24,
             'axis_font_size': 12,
             'value_font_size': 20
             },
    'currentEmp10': {
             'filename': 'currentEmp10.csv',
             'plot_type': 'bar',
             'y1_axis': 'percentage',
             'y2_axis': False,
             'x_title': False,
             'x_rot': 0,
             'x_max_len': 15,
             'y_title': 'Percentage',
             'chart_title': 'What type of contract?',
             'show_values': True,
             'skip_labels': False,
             'bottom_size': 0.15,
             'title_font_size': 24,
             'axis_font_size': 12,
             'value_font_size': 20
             },
    'currentEmp10p2': {
            'filename': 'currentEmp10p2.csv',
            'plot_type': 'bar',
            'y1_axis': 'percentage',
            'y2_axis': False,
            'x_title': False,
            'x_rot': 0,
            'x_max_len': 15,
            'y_title': 'Percentage',
            'chart_title': 'What type of contract?',
            'show_values': True,
            'skip_labels': False,
            'bottom_size': 0.15,
            'title_font_size': 24,
            'axis_font_size': 12,
            'value_font_size': 20
             },
    'rse1': {
            'filename': 'rse1.csv',
            'plot_type': 'bar',
            'y1_axis': 'percentage',
            'y2_axis': False,
            'x_title': False,
            'x_rot': 0,
            'x_max_len': 15,
            'y_title': 'Percentage',
            'chart_title': 'Do you write code?',
            'show_values': True,
            'skip_labels': False,
            'bottom_size': 0.15,
            'title_font_size': 24,
            'axis_font_size': 12,
            'value_font_size': 20
            },
    'rse3': {
            'filename': 'rse3.csv',
            'plot_type': 'bar',
            'y1_axis': 'percentage',
            'y2_axis': False,
            'x_title': False,
            'x_rot': 0,
            'x_max_len': 15,
            'y_title': 'Percentage',
            'chart_title': 'Who uses your code?',
            'show_values': True,
            'skip_labels': False,
            'bottom_size': 0.15,
            'title_font_size': 24,
            'axis_font_size': 14,
            'value_font_size': 24
            },
    'paper1': {
            'filename': 'paper1.csv',
            'plot_type': 'bar',
            'y1_axis': 'percentage',
            'y2_axis': False,
            'x_title': False,
            'x_rot': 0,
            'x_max_len': 15,
            'y_title': 'Percentage',
            'chart_title': 'Has your code contributed to a publication?',
            'show_values': True,
            'skip_labels': False,
            'bottom_size': 0.15,
            'title_font_size': 24,
            'axis_font_size': 14,
            'value_font_size': 20
            },
    'paper1p2': {
            'filename': 'paper1p2.csv',
            'plot_type': 'bar',
            'y1_axis': 'percentage',
            'y2_axis': False,
            'x_title': False,
            'x_rot': 0,
            'x_max_len': 15,
            'y_title': 'Percentage',
            'chart_title': 'Were you acknowledged?',
            'show_values': True,
            'skip_labels': False,
            'bottom_size': 0.15,
            'title_font_size': 24,
            'axis_font_size': 14,
            'value_font_size': 20
             },
    'train1': {
            'filename': 'train1.csv',
            'plot_type': 'bar',
            'y1_axis': 'percentage',
            'y2_axis': False,
            'x_title': False,
            'x_rot': 0,
            'x_max_len': 15,
            'y_title': 'Percentage',
            'chart_title': 'Have you trained researchers?',
            'show_values': True,
            'skip_labels': False,
            'bottom_size': 0.15,
            'title_font_size': 24,
            'axis_font_size': 14,
            'value_font_size': 20
            },
    'stability1': {
            'filename': 'stability1.csv',
            'plot_type': 'bar',
            'y1_axis': 'percentage',
            'y2_axis': False,
            'x_title': False,
            'x_rot': 0,
            'x_max_len': 15,
            'y_title': 'Percentage',
            'chart_title': 'Bus factor',
            'show_values': True,
            'skip_labels': False,
            'bottom_size': 0.15,
            'title_font_size': 24,
            'axis_font_size': 14,
            'value_font_size': 20
            },
    'stability2': {
            'filename': 'stability2.csv',
            'plot_type': 'bar',
            'y1_axis': 'percentage',
            'y2_axis': False,
            'x_title': False,
            'x_rot': 0,
            'x_max_len': 15,
            'y_title': 'Percentage',
            'chart_title': 'Technical handover plan?',
            'show_values': True,
            'skip_labels': False,
            'bottom_size': 0.15,
            'title_font_size': 24,
            'axis_font_size': 14,
            'value_font_size': 20
            },
    'stability3': {
            'filename': 'stability3.csv',
            'plot_type': 'bar',
            'y1_axis': 'percentage',
            'y2_axis': False,
            'x_title': False,
            'x_rot': 0,
            'x_max_len': 15,
            'y_title': 'Percentage',
            'chart_title': 'Have you released under Open Source?',
            'show_values': True,
            'skip_labels': False,
            'bottom_size': 0.15,
            'title_font_size': 24,
            'axis_font_size': 14,
            'value_font_size': 20
             },
    'socio3': {
            'filename': 'socio3.csv',
            'plot_type': 'bar',
            'y1_axis': 'RSEs',
            'y2_axis': 'Research community',
            'x_title': False,
            'x_rot': 0,
            'x_max_len': 10,
            'y_title': 'Percentage',
            'chart_title': 'Age',
            'show_values': True,
            'skip_labels': False,
            'bottom_size': 0.2,
            'title_font_size': 24,
            'axis_font_size': 14,
            'value_font_size': 15
            },
    'socio4': {
            'filename': 'socio4.csv',
            'plot_type': 'bar',
            'y1_axis': 'RSEs',
            'y2_axis': 'Research community',
            'x_title': False,
            'x_rot': 0,
            'x_max_len': 10,
            'y_title': 'Percentage',
            'chart_title': 'Salary',
            'show_values': True,
            'skip_labels': False,
            'bottom_size': 0.2,
            'title_font_size': 24,
            'axis_font_size': 14,
            'value_font_size': 15
            },
    'socio2': {
            'filename': 'socio2.csv',
            'plot_type': 'bar',
            'y1_axis': 'percentage',
            'y2_axis': False,
            'x_title': False,
            'x_rot': 0,
            'x_max_len': 15,
            'y_title': 'Percentage',
            'chart_title': 'Gender',
            'show_values': True,
            'skip_labels': False,
            'bottom_size': 0.15,
            'title_font_size': 24,
            'axis_font_size': 14,
            'value_font_size': 20
            },
    'socio5': {
            'filename': 'socio5.csv',
            'plot_type': 'bar',
            'y1_axis': 'percentage',
            'y2_axis': False,
            'x_title': False,
            'x_rot': 45,
            'x_max_len': 15,
            'y_title': 'Percentage',
            'chart_title': 'Ethnic origin',
            'show_values': True,
            'skip_labels': False,
            'bottom_size': 0.3,
            'title_font_size': 24,
            'axis_font_size': 14,
            'value_font_size': 20
             },
    }
    
    
    
    
    