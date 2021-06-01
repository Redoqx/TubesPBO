from prettytable import PrettyTable

x = PrettyTable()

x.field_names = ["City name", "Area", "Population", "Annual Rainfall"]

x.add_row(["Adelaide", 1295, 1158259, 600.5])
x.add_row(["Brisbane", 5905, 1857594, 1146.4])
x.add_row(["Darwin", 112, 120900, 1714.7])
x.add_row(["Hobart", 1357, 205556, 619.5])
x.add_row(["Sydney", 2058, 4336374, 1214.8])
x.add_row(["Melbourne", 1566, 3806092, 646.9])
x.add_row(["Perth", 5386, 1554769, 869.4])

def get_data_from_prettytable(data):
    """
    Get a list of list from pretty_data table
    Arguments:
        :param data: data table to process
        :type data: PrettyTable
    """

    def remove_space(liste):
        """
        Remove space for each word in a list
        Arguments:
            :param liste: list of strings
        """
        list_without_space = []
        for mot in liste:                                       # For each word in list
            word_without_space = mot.replace(' ', '')           # word without space
            list_without_space.append(word_without_space)       # list of word without space
        return list_without_space

    # Get each row of the table
    string_x = str(x).split('\n')                               # Get a list of row
    header = string_x[1].split('|')[1: -1]                      # Columns names
    rows = string_x[3:len(string_x) - 1]                        # List of rows

    list_word_per_row = []
    for row in rows:                                            # For each word in a row
        row_resize = row.split('|')[1:-1]                       # Remove first and last arguments
        list_word_per_row.append(remove_space(row_resize))      # Remove spaces

    return header, list_word_per_row

from fpdf import FPDF

def export_to_pdf(header, data):
    """
    Create a a table in PDF file from a list of row
        :param header: columns name
        :param data: List of row (a row = a list of cells)
        :param spacing=1:
    """
    pdf = FPDF()                                # New  pdf object

    pdf.set_font("Arial", size=12)              # Font style
    epw = pdf.w - 2*pdf.l_margin                # Witdh of document
    col_width = pdf.w / 4.5                     # Column width in table
    row_height = pdf.font_size * 1.5            # Row height in table
    spacing = 1.3                               # Space in each cell

    pdf.add_page()                              # add new page

    pdf.cell(epw, 0.0, 'My title', align='C')   # create title cell
    pdf.ln(row_height*spacing)                  # Define title line style

    # Add header
    for item in header:                         # for each column
        pdf.cell(col_width, row_height*spacing, # Add a new cell
                 txt=item, border=1)
    pdf.ln(row_height*spacing)                  # New line after header

    for row in data:                            # For each row of the table
        for item in row:                        # For each cell in row
            pdf.cell(col_width, row_height*spacing, # Add cell
                    txt=item, border=1)
        pdf.ln(row_height*spacing)              # Add line at the end of row

    pdf.output('simple_demo.pdf')               # Create pdf file
    pdf.close()                                 # Close file

header, data = get_data_from_prettytable(x)
export_to_pdf(header, data)
