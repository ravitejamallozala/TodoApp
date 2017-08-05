from django.core.management.base import BaseCommand, CommandError
from todoapp.models import Todolist
from todoapp.models import Todoitem
import click
class Command(BaseCommand):
    help="helps in loading db"
    def handle(self, *args, **options):
        names = ["ravi", "yatheendra sai", "sree pavan", "akshay", "mac"]
        descriptions = ["buy car", "buy bike", "walk on moon", "jump to jupiter", "sit on saturn"]
        click.echo("Here creating lists ans items")
        for j in range(5):
            c = Todolist(name=names[j])
            c.save()
            for i in range(5):
                c2 = Todoitem(description=descriptions[i], todolist=c)
                c2.save()