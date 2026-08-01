import asyncio
from rich.console import Console
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, TextColumn
from src.services.xray_manager import download_xray
from src.services.blocklist import fetch_ru_blocklist
from src.services.scraper import scrape_all
from src.services.validator import validate_all_xray
from src.services.generator import generate_outputs_old
from src.readme_builder import build_readme
from src.config import CORE_DIR, CONFIGS_DIR

console = Console()

def ensure_dirs():
    CORE_DIR.mkdir(parents=True, exist_ok=True)
    CONFIGS_DIR.mkdir(parents=True, exist_ok=True)

async def async_main():
    console.print(Panel.fit("[bold green]Free_VPN_Aggregator V3 Pro[/bold green]\n[dim]Starting Enterprise Xray-Core pipeline...[/dim]"))
    
    ensure_dirs()

    with Progress(SpinnerColumn(), TextColumn("[progress.description]{task.description}"), transient=True) as p:
        p.add_task(description="[cyan]Скачивание Xray-core и Blocklist...", total=None)
        await download_xray()
        blocked_ips = await fetch_ru_blocklist()

    with Progress(SpinnerColumn(), TextColumn("[progress.description]{task.description}"), transient=True) as p:
        p.add_task(description="[cyan]Сбор сырых конфигураций...", total=None)
        raw_configs = await scrape_all()

    if not raw_configs:
        console.print("[bold red][ERR] Сборщик не нашел конфигураций для проверки. Работа завершена.[/bold red]")
        return

    console.print(f"[green][OK][/green] Собрано сырых ссылок: [bold yellow]{len(raw_configs)}[/bold yellow]")

    with Progress(SpinnerColumn(), TextColumn("[progress.description]{task.description}"), transient=True) as p:
        p.add_task(description="[cyan]Xray-core валидация (HTTP-маршрутизация и DPI Bypass)...", total=None)
        working_configs = await validate_all_xray(raw_configs, blocked_ips, batch_size=100)

    console.print(f"[green][OK][/green] Идеально рабочих узлов найдено: [bold green]{len(working_configs)}[/bold green]")

    with Progress(SpinnerColumn(), TextColumn("[progress.description]{task.description}"), transient=True) as p:
        p.add_task(description="[cyan]Геолокация узлов...", total=None)
        import aiohttp
        from src.utils import batch_geoip_lookup
        async with aiohttp.ClientSession() as session:
            await batch_geoip_lookup(working_configs, session)

    from src.services.qr_generator import generate_all_qrs

    with Progress(SpinnerColumn(), TextColumn("[progress.description]{task.description}"), transient=True) as p:
        p.add_task(description="[cyan]Генерация форматов и QR-кодов...", total=None)
        generate_outputs_old(working_configs)
        generate_all_qrs()

    build_readme()
    
    console.print(Panel.fit("[bold green]Пайплайн V3 успешно завершен![/bold green]"))


def main():
    asyncio.run(async_main())

if __name__ == "__main__":
    main()
