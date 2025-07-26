import tkinter as tk
from tkinter import filedialog, messagebox
from PyPDF2 import PdfMerger

class PDFMergerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("PDF Merger Tool")
        self.root.geometry("500x400")
        self.pdf_files = []

        tk.Label(root, text="PDF Merger", font=("Times New Roman", 20, "underline")).pack(pady=10)

        self.listbox = tk.Listbox(root, width=60, height=10)
        self.listbox.pack(pady=10)

        tk.Button(root, text="Select PDF Files", command=self.add_pdfs, bg="#4CAF50", fg="white").pack(pady=5)
        tk.Button(root, text="Merge selected files", command=self.merge_pdfs, bg="#2196F3", fg="white").pack(pady=20)
        tk.Button(root, text="Clear List", command=self.clear_list, bg="#f4db36", fg="white").pack(pady=5)

    def add_pdfs(self):
        files = filedialog.askopenfilenames(filetypes=[("PDF Files", "*.pdf")])
        for file in files:
            if file not in self.pdf_files:
                self.pdf_files.append(file)
                self.listbox.insert(tk.END, file)

    def clear_list(self):
        self.pdf_files.clear()
        self.listbox.delete(0, tk.END)

    def merge_pdfs(self):
        if not self.pdf_files:
            messagebox.showwarning("Warning", "No PDF files selected.")
            return

        output_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF File", "*.pdf")])
        if not output_path:
            return

        try:
            merger = PdfMerger()
            for pdf in self.pdf_files:
                merger.append(pdf)
            merger.write(output_path)
            merger.close()
            messagebox.showinfo("Success", f"Merged PDF saved to:\n{output_path}")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred:\n{e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = PDFMergerApp(root)
    root.mainloop()