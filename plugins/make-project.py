# -*- Mode:Python; indent-tabs-mode:t; tab-width:4 -*-

import snapcraft

class MakeHandler(snapcraft.BaseHandler):
	def pull(self):
		return self.pullBranch(self.options.source)
	def build(self):
		return self.run("make all")
	def stage(self):
		return self.run("make install DESTDIR=" + self.stagedir)
	def deploy(self):
		return self.doDeploy(["bin", "share", "lib"]) # not "include"
	def test(self):
		return self.run("make check")