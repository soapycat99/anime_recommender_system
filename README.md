This data set contains information on user preference data from 73,516 users on 12,294 anime. Each user is able to add anime to their completed list and give it a rating and this data set is a compilation of those ratings.

Animea Dataset

| Column Name | Description                                                    |
|-------------|----------------------------------------------------------------|
| `anime_id`  | myanimelist.net's unique id identifying an anime.              |
| `name`      | full name of anime.                                            |
| `genre`     | comma separated list of genres for this anime.                 |
| `type`      | movie, TV, OVA, etc.                                           |
| `episodes`  | how many episodes in this show. (1 if movie).                  |
| `rating`    |  average rating out of 10 for this anime.                      |
| `members`   | number of community members that are in this anime's "group".  |

Rating Dataset(Because of its large volume, it's not able to be uploaded onto github)

| Column Name | Description                                                                        |
|-------------|------------------------------------------------------------------------------------|
| `user_id`   | non identifiable randomly generated user id.                                       |
| `anime_id`  | the anime that this user has rated.                                                |
| `rating`    | rating out of 10 this user has assigned (-1 if the user watched without assigning) |

**Goal**:
Building a better anime recommendation system based only on similiar anime. 

**Formula:**

![](https://cdn-images-1.medium.com/max/579/1*5hJibEtQPavnbgRxg8w2Fg.gif)

Cosine similarity measures the similarity between two vectors of an inner product space. It is measured by the cosine of the angle between two vectors and determines whether two vectors are pointing in roughly the same direction
