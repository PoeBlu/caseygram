# caseygram
caseygram is a Instagram clone built using Django, Bootstrap, and jQuery. I recreated many of Instagrams features including: CRUD capabilties on posts, explore page, likes, comments, direct messaging, profiles, profiles pictures, bios, search bar, and followers/following categories. I used Bootstrap to recreate the UX of instagrams desktop page that changes for mobile use. jQuery is used to make real time like/follower/follwing updates using AJAX calls. Check out the website at (https://caseygram.herokuapp.com/)!
## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.


## Unit Tests

I have a handful of unit tests written for testing messages and posts.

```
class MessageTestCase(TestCase):

    def create_message(self, sender=User.objects.get(id=1), receiver=User.objects.get(id=2), content='test message'):
        return Message.objects.create(sender=sender, receiver=receiver, content=content, date_created=timezone.now())

    def test_message_creation(self):
        message = self.create_message()
        self.assertTrue(isinstance(message, Message))
        self.assertEqual(message.__str__(), message.content)
```

## Deployment

caseygram is deployed on Heroku.

## Built With

* [Django](https://www.djangoproject.com/) - The web framework used
* [Bootstrap](https://getbootstrap.com/) - Frontend html/css classes
* [jQuery](https://jquery.com/) - Used for AJAX calls
* [Heroku](https://www.heroku.com/) - Used for deployment

## Authors

* **Casey DeLange** - [cdelange](https://github.com/cdelange)


## Acknowledgments
* Excited to finish this project!
* Corey Schafer- [Corey's Youtube channel](https://www.youtube.com/channel/UCCezIgC97PvUuR4_gbFUs5g) His youtube channel helped me learn Django in no time!

