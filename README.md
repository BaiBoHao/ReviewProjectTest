# ReviewProjectTest

This is a deliberately small, synthetic repository used to validate
[ByteCodeReviewAgent](https://github.com/BaiBoHao/ByteCodeReviewAgent).

The `main` branch contains a safe baseline. Pull-request branches may introduce intentionally
flawed code so the review agent can be tested against realistic diffs. All credentials and data
in this repository are fictional.

## Run tests

```bash
python -m pip install -e .
python -m unittest discover -s tests -v
```
