# Advent of Code

This is my repository for my [Advent of Code](https://adventofcode.com/) solutions. The framework is a clone of [David Brownman´s](https://github.com/xavdid/advent-of-code).

## Quickstart

This repo has two main executables: `start` and `advent`. See David´s repo for instructions. The only difference is that I added an additional argument so that I can specify the input file. Now I can either run test.txt or input.txt

## ./advent

### Usage

> `./advent [-h] [--year year] [--slow] [--debug] [--profile] day`

Run a day of Advent of Code

positional arguments:

- `day` (required): Which puzzle day to run

optional arguments:

- `-h, --help` (optional): show this help message and exit
- `--year YEAR` (optional): Puzzle year. Defaults to current year if December has begun, otherwise previous year
- `--file` (optional): specify the input file to be used 
`--slow` (optional): specify that long-running solutions (or those requiring manual input) should be run
- `--debug` (optional): prints normally-hidden debugging statements
- `--profile` (optional): run solution through a performance profiler

### Examples

- `./advent 2`
- `./advent 5 --year 2020 --file test.txt
- `./advent 5 --year 2020 --file input.txt`
- `./advent 3 --slow`

### Reading Input

AoC input takes a number of forms, so there are a number of simple modes in which input can be read. Pick a mode by setting `Solution.input_type` to one of the following `Enum` values:

| InputTypes.X | description                                             | input for this mode   |
| ------------ | ------------------------------------------------------- | --------------------- |
| TEXT         | one solid block of text; the default                    | `abcde`               |
| INTEGER      | one number                                              | `12345`               |
| TSV          | tab-separated values                                    | `a b c`<br>`d e f`    |
| STRSPLIT     | str[], split by a specified separator (default newline) | a<br>b<br>c<br>d<br>e |
| INTSPLIT     | int[], split by a specified separator (default newline) | 1<br>2<br>3<br>4<br>5 |

Specify `Solution.separator` to control how the SPLIT methods separate their input.

