## Reproducibility Pytests

These pytests are used for reproducibility CI checks in the [ACCESS-NRI/reproducibility](https://github.com/ACCESS-NRI/reproducibility) repository. Code from these tests is adapted from COSIMAS's ACCESS-OM2's [
bit reproducibility tests](https://github.com/COSIMA/access-om2/blob/master/test/test_bit_reproducibility.py).

### How to run tests manually

1. First clone the pytest code which is on the `main` branch of `access-om2-configs` repository into a separate directory.
```sh
git clone https://github.com/ACCESS-NRI/access-om2-configs/ test-code
```

2. Checkout an experiment
```sh
git clone https://github.com/ACCESS-NRI/accessom2-configs/ <experiment>
cd <experiment>
git checkout <branch/tag>
```

3. Setup payu
```sh
module use /g/data/vk83/modules
module load payu/1.1
```

4. Run the pytests
```sh
pytest <path/to/test-code>/test
```

### Pytest Options

The output directory for pytests output defaults to `/scratch/$PROJECT/$USER/test-model-repro` and contains the following sub-directories:
- `control` - contains copies of the model configuration used for each experiment run in the tests.
- `lab` - contains `payu` model output directories containing `work` and `archive` sub-directories.

This output directory also contains files generated in pytests. This includes the `CHECKSUM` file which is used as part of reproducibility CI workflows.

To set pytest output code to a different folder, use `--output-path` command flag, for example:

```sh
pytest <path/to/test-code>/test --output-path /some/other/path/for/output
```

By default, the control directory, e.g. the model configuration to test, is the current working directory. This can be set similarly to above by using the 
`--control-path` command flag.

The path containing the checksum file to check against can also be set using
`--checksum-path` command flag. The default is the `testing/checksum/CHECKSUM`
file which is stored in the control directory.

To run only checks run as part of CI reproducibility checksum tests, use `-m checksum`, e.g.

```sh
pytest <path/to/test-code>/test -m checksum
```
