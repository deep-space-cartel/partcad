# Notes

## Suggestions

* There is no Quick Start section on https://partcad.org/
  * - You can not wait, think "fly" - Jake's First Flight On Ikran

## Questions

* What is `build123d` in `OCP CAD VIEWER`
* What is `CadQuery` in `OCP CAD VIEWER`
* Can `OCP CAD VIEWER` use existing Python virtual env?
* Why `conda`?

## Problems

```
ERROR: OpenSCAD executable is not found. Please, install OpenSCAD first.
```

* It's an error from tutorial. Solution is `sudo apt-get install openscad`.


## Related issues

* [Poetry glibc version check](https://github.com/python-poetry/poetry/issues/9837)


```bash
python -m cProfile -o pc-version.prof $(command -v pc) version
flameprof -o /tmp/pc-version.svg -r $(command -v pc) version
```

```bash
conda info --envs
conda create -n ocp-cad-viewer python=3.10
conda activate ocp-cad-viewer
```

```bash
"/home/vscode/miniconda3/envs/ocp-cad-viewer/bin/python" -m pip install ocp_vscode==2.6.1 git+https://github.com/gumyr/build123d ## && exit
```

```bash
env -u CONDA_PREFIX_1  "/home/vscode/miniconda3/envs/ocp-cad-viewer/bin/python" -m pip install ocp_vscode==2.6.1 git+https://github.com/cadquery/cadquery.git && exit
```
