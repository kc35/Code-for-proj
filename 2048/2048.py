if __name__ == "__main__":
   # ==== preparing main window
   app = Play_2048()
   app.bind_all('<Key>', app.moves)
   app.wm_title("2048 by PythonGeeks")
   app.minsize(430, 470)
   app.mainloop()
