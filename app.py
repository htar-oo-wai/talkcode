from ui.layout import build_interface

def main():
    demo = build_interface()
    demo.queue(max_size=99).launch(debug=True)

if __name__ == "__main__":
    main()
