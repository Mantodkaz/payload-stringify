# payload stringify

`payload-stringify` is a lightweight tool that converts any text-based payload like `ASPX, PHP, HTML, JS, JSON, Shell Script into C-style string literals.` useful for embedding payloads directly into C/C++ projects like custom droppers, implants, or loaders.

## Features

- Supports any UTF-8 text file
- Output ready to be copy-pasted into a `const char*` declaration in C/C++
- Lightweight, no external dependencies

## Why?

Sometimes you need to embed your payload (e.g., a webshell, HTML beacon, or one-liner loader) directly inside a C/C++ binary. This tool helps you convert those files into clean, compile-ready string literals.

## Example

### Input (`backdoor.aspx`)
```aspx
<%@ Page Language="C#" %>
<script runat="server">
    Response.Write("heyyaaa");
</script>
```
##  Not Supported
- Binary files (.exe, .dll, .png, etc)
- Files with non-UTF8 encodings (e.g., UTF-16)
