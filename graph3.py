import xlsxwriter

workbook = xlsxwriter.Workbook('oo.xlsx')
worksheet = workbook.add_worksheet()
bold = workbook.add_format({'bold': 1})

# Add the worksheet data that the charts will refer to.
headings = ['Number', 'Batch 1', 'Batch 2']
data = [[1,2,3,4,5,7,8],
       [0,3,8,15,24,35,48,63]]
 

worksheet.write_row('A1', headings, bold)
worksheet.write_column('A2', data[0])
worksheet.write_column('B2', data[1])


# Create a new chart object. In this case an embedded chart.
chart1 = workbook.add_chart({'type': 'line'})

# Configure the first series.
chart1.add_series({
    'name':       '=Sheet1!$B$1',
    'categories': '=Sheet1!$A$2:$A$7',
    'values':     '=Sheet1!$B$2:$B$7',})

# Configure second series. Note use of alternative syntax to define ranges.
chart1.add_series({
    'name':       ['Sheet1', 0, 2],
    'categories': ['Sheet1', 1, 0, 6, 0],
    'values':     ['Sheet1', 1, 2, 6, 2],})

# Add a chart title and some axis labels.
chart1.set_title ({'name': 'Results of sample analysis'})
chart1.set_x_axis({'name': 'Test number'})
chart1.set_y_axis({'name': 'Sample length (mm)'})

# Set an Excel chart style. Colors with white outline and shadow.
chart1.set_style(10)

# Insert the chart into the worksheet (with an offset).
worksheet.insert_chart('D2', chart1, {'x_offset': 25, 'y_offset': 10})


workbook.close()

