# comics_to_vk

## This is an assistant for publishing comics to group wall in VK, it can:
- Download images from [https://xkcd.com/](https://xkcd.com/)
- Publish images group wall in [VK](https://vk.com/)

## Installing required dependencies
- [Create community](https://vk.com/groups?tab=admin)
- [Create App in VK](https://vk.com/editapp?act=create)

![create_app](https://user-images.githubusercontent.com/105148929/187678988-016d5813-4785-41ea-bb18-119eb1f44fa3.png)

- Next step, copy the `client_id` in the address bar 

![client_id](https://user-images.githubusercontent.com/105148929/187686901-f24244d5-4f22-4d28-ae80-1695c3760b84.png)

- The next step, you need to get an `access_token`, do the following:
 1. Open project directory from `cmd`
 ```
 $ python get_token_vk.py <client_id>
 ```
 `<client_id>` - this is positional argument `client_id` from previous step
In response you will receive an URL

 2. Copy the url to the address bar of your browser, then click `Allow`
 
 ![for_access_token](https://user-images.githubusercontent.com/105148929/187713569-ebb15c98-9c2e-47b8-8546-63bbc94513bf.png)

 3. Next in the address bar you will see your `access_token`, look like this `vk1.a._DDdsoQNAr6Lfm_ZBnCZuXzwkILfnx73JLH05gQFVwavJK_ewuUmJdVQR`
 
- The next step, you need to get an `group_id`, do the following from `cmd:
 ```
 $ python get_group_id.py <access_token>
 ```
 `<access_token>` - this is positional argument `access_token` from previous step.
 In response you will receive an `group_id`
 
## Setting environment variables
* Create `.env` file in project directory and write:
```
ACCESS_TOKEN=Your_access_token
GROUP_ID=Your_group_id
```		
### Requirements
* python-dotenv==0.20.0
* requests==2.28.1

     
Remember, it is recommended to use [virtualenv/venv](https://docs.python.org/3/library/venv.html) for better isolation.
Python3 should be already installed. Then use pip (or pip3, if there is a conflict with Python2) to install dependencies:
```
pip install -r requirements.txt
```		
## Application launch

### Open project directory from cmd

#### Publication random comics to wall your community: 
```
$ python main.py 
```

So well done=) You can look result in your wall group

![result](https://user-images.githubusercontent.com/105148929/187718000-63ee0f52-0c8b-45e5-b89a-27f216b78504.png)


*Project Goals*
	
*Make blogging life easier*
