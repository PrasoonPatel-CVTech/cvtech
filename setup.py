from distutils.core import setup

setup(
  name = 'cvtech',         # How you named your package folder (MyLib)
  packages = ['cvtech'],   # Chose the same as "name"
  version = '1.4',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'AI based Computer Vision Library by cvtech',   # Give a short description about your library
  author = 'Prasoon Patel',                   # Type in your name
  author_email = 'prasoon_patel@live.com',      # Type in your E-Mail
  url = 'https://github.com/PrasoonPatel-CVTech/cvtech',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/PrasoonPatel-CVTech/cvtech/archive/refs/heads/master.zip',    # I explain this later on
  keywords = ['ComputerVision', 'HandTracking', 'HandDetection'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'opencv-python',
          'mediapipe',
          'numpy',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
  ],
)