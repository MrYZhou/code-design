pyinstaller --onefile --noconfirm  ^
--windowed --clean --name "pyparser" ^
--add-data "./static;static/" ^
--add-data "./main.py;."  "./main.py"


@REM pyinstaller  --onedir --console --name "pyparser"  --clean ^
@REM     --add-data "./static;static/" ^
@REM     --add-data "./main.py;." "./main.py" ^
  