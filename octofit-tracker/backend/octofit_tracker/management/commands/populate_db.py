from django.core.management.base import BaseCommand

from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Delete existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create Teams
        marvel = Team.objects.create(name='Marvel', members=[])
        dc = Team.objects.create(name='DC', members=[])

        # Create Users
        users = [
            User.objects.create(name='Iron Man', email='ironman@marvel.com', team='Marvel'),
            User.objects.create(name='Captain America', email='cap@marvel.com', team='Marvel'),
            User.objects.create(name='Spider-Man', email='spiderman@marvel.com', team='Marvel'),
            User.objects.create(name='Batman', email='batman@dc.com', team='DC'),
            User.objects.create(name='Superman', email='superman@dc.com', team='DC'),
            User.objects.create(name='Wonder Woman', email='wonderwoman@dc.com', team='DC'),
        ]

        # Add users to team members
        marvel.members = [u.email for u in users if u.team == 'Marvel']
        marvel.save()
        dc.members = [u.email for u in users if u.team == 'DC']
        dc.save()

        # Create Workouts
        workouts = [
            Workout.objects.create(name='Push Ups', description='Upper body workout', difficulty='Medium'),
            Workout.objects.create(name='Running', description='Cardio workout', difficulty='Easy'),
            Workout.objects.create(name='Squats', description='Leg workout', difficulty='Medium'),
        ]

        # Create Activities
        Activity.objects.create(user=users[0].email, activity_type='Push Ups', duration=30, date='2024-01-01')
        Activity.objects.create(user=users[1].email, activity_type='Running', duration=45, date='2024-01-02')
        Activity.objects.create(user=users[2].email, activity_type='Squats', duration=20, date='2024-01-03')
        Activity.objects.create(user=users[3].email, activity_type='Push Ups', duration=25, date='2024-01-04')
        Activity.objects.create(user=users[4].email, activity_type='Running', duration=35, date='2024-01-05')
        Activity.objects.create(user=users[5].email, activity_type='Squats', duration=40, date='2024-01-06')

        # Create Leaderboard
        Leaderboard.objects.create(team='Marvel', points=270)
        Leaderboard.objects.create(team='DC', points=250)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
