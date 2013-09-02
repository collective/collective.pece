from collective.cover.tiles.banner import BannerTile
from plone.directives import form
from plone.namedfile.field import NamedBlobImage
from zope.schema import TextLine


class IImageArtifact(form.Schema):
    """
    Content type
    """

    # XXX Must be called 'image' to work with c.cover
    image = NamedBlobImage(title=u"Image Artifact")
    form.primary('image')

    coverage = TextLine(title=u"Coverage", required=False)

    dublin_core_format = TextLine(title=u"Format", required=False)

    identifier = TextLine(title=u"Identifier", required=False)

    language = TextLine(title=u"Language", required=False)

    publisher = TextLine(title=u"Publisher", required=False)

    relation = TextLine(title=u"Relation", required=False)

    rights = TextLine(title=u"Rights", required=False)

    source = TextLine(title=u"Source", required=False)

    subject = TextLine(title=u"Subject", required=False)

    dublin_core_type = TextLine(title=u"Type", required=False)


# Monkey patch collective.cover
def accepted_ct():
    return ['Image', 'Link', 'image_artifact']


# Monkey patch collective.cover
def populate_with_object(obj):
    """Tile can be populated with images and links; in this case we're not
    going to take care of any modification of the original object; we just
    copy the data to the tile and deal with it.
    """
    if obj.context.portal_type not in accepted_ct():
        return

    super(banner.BannerTile, self).populate_with_object(obj.context)  # check permissions
    obj = aq_base(obj.context)  # avoid acquisition
    title = obj.context.Title()
    # if image, store a copy of its data
    if obj.context.portal_type == 'Image' or obj.context.portal_type == 'image_artifact':
        if hasattr(obj.context, 'getImage'):
            data = obj.context.getImage().data
        else:
            data = obj.context.image.data
        image = NamedBlobImage(data)
    else:
        image = None
    remote_url = obj.context.getRemoteUrl() if obj.context.portal_type == 'Link' else None

    data_mgr = ITileDataManager(self)
    data_mgr.set({
        'title': title,
        'image': image,
        'remote_url': remote_url,
    })
