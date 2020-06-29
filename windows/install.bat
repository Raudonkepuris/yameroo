md "C:\Program Files\yameroo"
SET path=%~dp0
copy %path%\*.py "C:\Program Files\yameroo"
md "C:\Program Files\yameroo\animewallpapers"
md "C:\Program Files\yameroo\hentais"
md "C:\Program Files\yameroo\config"
copy %path%\config.yaml "C:\Program Files\yameroo\config"

PAUSE