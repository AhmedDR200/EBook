import random
from faker import Faker
from django.utils import timezone
from django.core.management.base import BaseCommand
from ...models import Ebook, Review

fake = Faker()

class Command(BaseCommand):
    help = 'Populate the database with dummy data'

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.SUCCESS('Creating dummy data...'))

        # Create dummy ebooks
        ebooks = []
        for _ in range(10):
            ebook = Ebook(
                title=fake.sentence(),
                author=fake.name(),
                description=fake.paragraph(),
                publication_date=fake.date_between(start_date='-2y', end_date='today')
            )
            ebooks.append(ebook)

        Ebook.objects.bulk_create(ebooks)

        # Create dummy reviews for each ebook
        for ebook in Ebook.objects.all():
            for _ in range(random.randint(1, 5)):
                review = Review(
                    review_author=fake.name(),
                    review=fake.paragraph(),
                    rating=random.randint(1, 5),
                    ebook=ebook
                )
                review.save()

        self.stdout.write(self.style.SUCCESS('Dummy data created successfully.'))
