class ProgramConfig:
    section: str
    pages: int = 1
    out_dir: Path = Path("data")
    headless: bool = True
    delay_ms: int = 1200
    jitter: float = 0.4
    max_retries: int = 2
    resume: bool = False
