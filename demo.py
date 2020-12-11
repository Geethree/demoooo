import logging
import os
import sys

import github3


class SyncR:
	def __init__(self, user, passs, repository):
		self.login_to_gh(user, passs)


	def login_to_gh(self, user, passs):
		github3.login(username=user, password=passs)

	def fetch_current_main(self):
		pass

	def check_for_local_changes(self,):
		self.fetch_current_main()

		self.diff_local_with_staging_are()

	def create_branch(self,):
		pass

	def commit(self,):
		pass

	def push_to_remote(self,):
		pass

	def create_pr():
		pass


if __name__== "__main__":
	repository = sys.argv[1]
	username = sys.argv[2]
	password = sys.argv[3]

	syncr = SyncR(username, password, repository)

	syncr.checkout_current_main()
	
	if(syncr.check_for_local_changes()):
		#if we have changes
		syncr.create_branch()
		syncr.commit()
		syncr.push_to_remote()
		syncr.create_pr()
		logging.log("Some useful log here")
	else:
		logging.info()


