from PyPDF2 import PdfFileMerger


class MergePDF:

    def __init__(self):
        self.merger = PdfFileMerger()
        self.docs = [
            item.lstrip() for item in input(
                "Input documents separated by a comma: "
                ).split(",")
            ]
        self.file_name = input("Enter the name of your output file: ")

    def merge(self):
        for doc in self.docs:
            try:
                self.merger.append(str(doc + ".pdf"))
            except Exception as e:
                print(e)
        with open(f"{self.file_name}.pdf", 'wb') as output_file:
            self.merger.write(output_file)


if __name__ == '__main__':
    MergePDF().merge()
