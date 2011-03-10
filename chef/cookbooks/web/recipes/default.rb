package "git-core"
package "python-dev"
package "python-setuptools"
package "postgresql-dev"
package "postgresql-client"
package "build-essential"
package "libpq-dev"
package "subversion"
package "mercurial"

template "/etc/apache2/apache2.conf" do
    source "apache2.conf"
    owner "root"
    group "root"
    mode "644"
end