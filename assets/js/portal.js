(function() {
    // Namespace
    window.AloboPortal = {
        init: function() {
            // Seed database if empty
            if (!localStorage.getItem('alobo_users')) {
                var defaultUsers = [
                    {
                        name: "Auma Florence",
                        email: "auma@gmail.com",
                        password: "password123",
                        ward: "Kengere"
                    }
                ];
                localStorage.setItem('alobo_users', JSON.stringify(defaultUsers));
            }
            if (!localStorage.getItem('alobo_requests')) {
                var defaultRequests = [
                    {
                        id: "SCE-26-401",
                        userEmail: "auma@gmail.com",
                        type: "Borehole Repair",
                        ward: "Kengere",
                        description: "The local borehole in Kengere Ward has been leaking and needs urgent repair to restore clean water access for 50+ households.",
                        phone: "+256 772 123456",
                        date: "2026-06-15",
                        status: "Resolved"
                    },
                    {
                        id: "SCE-26-405",
                        userEmail: "auma@gmail.com",
                        type: "Bursary Inquiry",
                        ward: "Kengere",
                        description: "Requesting details on the application process and deadlines for the Soroti City East Secondary School bursaries for the upcoming term.",
                        phone: "+256 772 123456",
                        date: "2026-07-01",
                        status: "In Progress"
                    }
                ];
                localStorage.setItem('alobo_requests', JSON.stringify(defaultRequests));
            }
            if (!localStorage.getItem('alobo_raised_amount')) {
                localStorage.setItem('alobo_raised_amount', '12750000');
            }
            if (!localStorage.getItem('alobo_donors_count')) {
                localStorage.setItem('alobo_donors_count', '1247');
            }
        },

        getUsers: function() {
            this.init();
            return JSON.parse(localStorage.getItem('alobo_users') || '[]');
        },

        getRequests: function() {
            this.init();
            return JSON.parse(localStorage.getItem('alobo_requests') || '[]');
        },

        getCurrentUser: function() {
            var email = localStorage.getItem('alobo_current_user');
            if (!email) return null;
            var users = this.getUsers();
            for (var i = 0; i < users.length; i++) {
                if (users[i].email === email) {
                    return users[i];
                }
            }
            return null;
        },

        register: function(name, email, password, ward) {
            var users = this.getUsers();
            // Check if user exists
            for (var i = 0; i < users.length; i++) {
                if (users[i].email.toLowerCase() === email.toLowerCase()) {
                    return { success: false, message: "An account with this email already exists." };
                }
            }
            var newUser = { name: name, email: email, password: password, ward: ward };
            users.push(newUser);
            localStorage.setItem('alobo_users', JSON.stringify(users));
            // Log in user
            localStorage.setItem('alobo_current_user', email);
            return { success: true };
        },

        login: function(email, password) {
            var users = this.getUsers();
            for (var i = 0; i < users.length; i++) {
                if (users[i].email.toLowerCase() === email.toLowerCase() && users[i].password === password) {
                    localStorage.setItem('alobo_current_user', users[i].email);
                    return { success: true };
                }
            }
            return { success: false, message: "Invalid email or password." };
        },

        logout: function() {
            localStorage.removeItem('alobo_current_user');
        },

        getUserRequests: function(email) {
            var allRequests = this.getRequests();
            return allRequests.filter(function(r) {
                return r.userEmail.toLowerCase() === email.toLowerCase();
            });
        },

        createRequest: function(userEmail, type, ward, description, phone) {
            var requests = this.getRequests();
            var randomId = Math.floor(100 + Math.random() * 900);
            var id = "SCE-26-" + randomId;
            var date = new Date().toISOString().split('T')[0];
            var newRequest = {
                id: id,
                userEmail: userEmail,
                type: type,
                ward: ward,
                description: description,
                phone: phone,
                date: date,
                status: "Under Review"
            };
            requests.unshift(newRequest); // Add to beginning
            localStorage.setItem('alobo_requests', JSON.stringify(requests));
            return { success: true, request: newRequest };
        },

        getFundStats: function() {
            this.init();
            return {
                goal: 50000000,
                raised: parseInt(localStorage.getItem('alobo_raised_amount') || '12750000'),
                donors: parseInt(localStorage.getItem('alobo_donors_count') || '1247'),
                days: 46
            };
        },

        addDonation: function(amount) {
            var stats = this.getFundStats();
            var newRaised = stats.raised + amount;
            var newDonors = stats.donors + 1;
            localStorage.setItem('alobo_raised_amount', newRaised.toString());
            localStorage.setItem('alobo_donors_count', newDonors.toString());
            return {
                goal: stats.goal,
                raised: newRaised,
                donors: newDonors,
                days: stats.days
            };
        }
    };

        // Form submission handler for wf-form-custom forms
        // Replaces Webflow's built-in w-form handler that relied on data-wf-element-id
        initFormHandlers: function() {
            var self = this;
            // Reset any stale success/fail states from browser back-forward cache
            document.querySelectorAll('.wf-form-custom .w-form-done').forEach(function(el) {
                el.style.display = 'none';
            });
            document.querySelectorAll('.wf-form-custom form').forEach(function(el) {
                el.style.display = '';
            });
            // Attach submit handlers to all wf-form-custom forms
            document.querySelectorAll('.wf-form-custom form').forEach(function(form) {
                // Skip forms with action attribute (external submissions like Formspree)
                if (form.getAttribute('action')) return;
                form.addEventListener('submit', function(e) {
                    e.preventDefault();
                    var container = form.closest('.wf-form-custom');
                    if (!container) return;
                    var doneDiv = container.querySelector('.w-form-done');
                    var failDiv = container.querySelector('.w-form-fail');
                    // Basic email validation
                    var emailInput = form.querySelector('input[type="email"]');
                    if (emailInput && emailInput.value) {
                        var emailRegex = /^\S+@\S+$/;
                        if (!emailRegex.test(emailInput.value)) {
                            if (failDiv) {
                                failDiv.style.display = 'block';
                            }
                            return;
                        }
                    }
                    // Show success, hide form
                    if (doneDiv) {
                        doneDiv.style.display = 'block';
                        form.style.display = 'none';
                    }
                });
            });
        }
    };
    window.AloboPortal.init();
    window.AloboPortal.initFormHandlers();
})();
