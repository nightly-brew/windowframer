# windowframer
windowframer is a python utility that takes care of drawing border images compatible with the [sway-borders] project.

Currently only one frame type is implemented, though additional types can be implemented easily.

| frame type | produces                                                                                     |
|------------|----------------------------------------------------------------------------------------------|
| rounded    | - perfectly square corners   <br>- perfectly round corners   <br>- rounded square corners    |

Each frame type has its own settings, use --help after specifying the type to list all available options.

## installation
windowframer depends on python3 and the [pycairo library].
After installing the dependencies, clone the repo and make the "windowframer.py" script executable.

## usage

### general usage
```sh
./windowframer.py <output_file> <frame_type> {specific_frame_patameters} [{optional_frame_parameters}]
```

example:
```sh
./windowframer.py test.png rounded --shadow_spread 4 5 0.4 #2E3440
```

### get help about a frame type
```sh
./windowframer.py <output_file> <frame_type> --help
```

example:
```sh
./windowframer.py test.png rounded --help
```

NOTICE: When using --help, nothing is really written to the specified output file.


[sway-borders]: https://github.com/fluix-dev/sway-borders
[pycairo library]: https://github.com/fluix-dev/sway-borders
