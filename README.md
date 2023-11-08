# auto-flu
Automated analysis of Mycobacterium tuberculosis (TB) Antimicrobial Resistance (AMR) amplicon sequence data using
the [BCCDC-PHL/AMR-TB-amplicon-artic-nf](https://github.com/BCCDC-PHL/AMR-TB-amplicon-artic-nf) pipeline.

# Installation

# Usage
Start the tool as follows:

```bash
auto-tb-amr-amplicon --config config.json
```

See the Configuration section of this document for details on preparing a configuration file.

More detailed logs can be produced by controlling the log level using the `--log-level` flag:

```bash
auto-tb-amr-amplicon --config config.json --log-level debug
```

# Configuration
This tool takes a single config file, in JSON format, with the following structure:

```json
{
  "fastq_by_run_dir": "/path/to/fastq_symlinks_by_run",
  "analysis_output_dir": "/path/to/analysis_by_run",
  "analysis_work_dir": "/path/to/work-auto-tb-amr-amplicon",
  "excluded_runs_list": "/path/to/excluded_runs.csv",
  "notification_email_addresses": [
	"someone@example.org",
	"someone_else@example.org"
  ],
  "send_notification_emails": true,
  "scan_interval_seconds": 3600,
  "pipelines": [
    {
      "pipeline_name": "BCCDC-PHL/AMR-TB-amplicon-artic-nf",
      "pipeline_version": "main",
      "pipeline_parameters": {
  	    "prefix": null,
   	    "bed": "/path/to/primers.bed",
   	    "ref": "/path/to/ref.fa",
	    "composite_ref": "/path/to/composite_ref.fa",
	    "references_amplicons": "/path/to/tbAMR_amplicons",
	    "references_amplicons_abscessus": "/path/to/abscessusAMR_amplicons",
	    "primer_pairs_tsv": "/path/to/primer_pairs.tsv",
	    "db": "/path/to/hsp65_database",
	    "directory": null,
	    "outdir": null
      }
    }
  ]
}
```

# Logging
This tool outputs [structured logs](https://www.honeycomb.io/blog/structured-logging-and-your-team/) in [JSON Lines](https://jsonlines.org/) format:

Every log line should include the fields:

- `timestamp`
- `level`
- `module`
- `function_name`
- `line_num`
- `message`

...and the contents of the `message` key will be a JSON object that includes at `event_type`. The remaining keys inside the `message` will vary by event type.

```json
{"timestamp": "2022-09-22T11:32:52.287", "level": "INFO", "module", "core", "function_name": "scan", "line_num", 56, "message": {"event_type": "scan_start"}}
```
