# Programming Lab Manual
This book is designed to be used as a programming reference for undergraduate physics students as they perform their practical laboratories. 

## Requirements
First, you are required to have a working version of the [Rust](https://www.rust-lang.org/learn) programming language with the cargo package manager included.

To build this book, it is required that you have a version of [mdbook](https://github.com/rust-lang/mdBook) installed.
The simplest way to do this is to use cargo:
``` sh
$ cargo install mdbook
```

## Building the Book
In order to render the book into html and view in your web browser:
``` sh
$ mdbook build
$ mdbook serve
```
The rendered html and other static files should now be in the `book` directory and you can to navigate to `http://localhost:3000` to see the book.
You can also view the book by opening `book/index.html` in your web browser.

