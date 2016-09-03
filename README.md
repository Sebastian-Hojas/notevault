I love to take notes and capture memories in an uncomplicated manner. Often I only take a screenshot or safe a file and store it in a folder. 
This little tool helps me to keep my memory vaults clean. Whenever a new file is added to the folder, it renames the file to `yyyy_MM_dd_filename`. The date is calculated from the file creation date, and for OSX screenshots the parsed date from the filename.

![example](https://github.com/Sebastian-Hojas/sortnote/blob/master/raw/example.png)

## Usage

The simplest way to sort an existing directory once is by using the `run` command:

```
sortnote run folder
```

If you want the tool to automatically sort your directory every hour, you can `enable` (or later `disable`) the tool:

```
sortnote enable folder
```

Use `-h` to see all options:

```
usage: sortnote [-h] [-d] [-v] [-Y]
                {enable,disable,run,reset,status} [directory]

Brings order to a chaotic world.

positional arguments:
  {enable,disable,run,reset,status}
                        Setups cron job for this directory
  directory

optional arguments:
  -h, --help            show this help message and exit
  -d, --dry             Dry run: Do not rename files, only print
  -v, --verbose         Verbose: Prints file rename descriptions
```

## Installation

Sortnote will be available through `pip`soon. In the meanwhile, you can install it by

```bash
python setup.py install
```

## Requirements 

The tool is based on a UNIX-cron system and runs on Python2.6.

## License

Sortnote is released under an MIT license. See [LICENSE](https://github.com/Sebastian-Hojas/sortnote/blob/master/LICENSE) for more information.